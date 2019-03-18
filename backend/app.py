from flask import Flask, Markup
from flask import (
    url_for,
    request, redirect,
    render_template,
    send_from_directory,
)
from werkzeug import secure_filename
from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import flask_admin as admin
from flask_admin.model import BaseModelView
from flask_admin.contrib.geoa import ModelView
from flask_admin.contrib.fileadmin import FileAdmin
from flask_admin.form import ImageUploadField

# Geoshapes in model
from geoalchemy2.types import Geometry
from geoalchemy2.shape import to_shape
import geojson, json

# Project formatting
import arrow
import markdown
MARKDOWN_EXT = ['markdown.extensions.tables']

# Gravatar
from urllib.parse import urlencode
import hashlib, codecs, datetime
import os.path as ospath
from os import urandom

# Create application
app = FlaskAPI(__name__, static_url_path='')
app.debug = True
app.config.from_pyfile('config.py')
app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Various presets
with open(ospath.join(ospath.dirname(__file__), 'templates','presets','project-status.json'), "r") as f:
    project_statuses = json.load(f)
screenshot_path = ospath.join(ospath.dirname(__file__), '..', 'screenshots')
upload_path = ospath.join(ospath.dirname(__file__), '..', 'uploads')
DEFAULT_THUMB = '../img/usermap.jpg'

# Create admin
admin = admin.Admin(app, name='SmartUse', template_mode='bootstrap3')

# ------------ Helper functions ------------

def get_media_type(filename):
    if filename.endswith('.gif'):
        return 'image/gif'
    if filename.endswith('.png'):
        return 'image/png'
    if filename.endswith('.jpg') or filename.endswith('.jpeg'):
        return 'image/jpeg'
    if filename.endswith('.geojson'):
        return 'application/vnd.geo+json'
    if filename.endswith('datapackage.json'):
        return 'application/vnd.datapackage+json'
    if filename.startswith('http'):
        return 'application/html'
    return None

def get_features_geojson(name, objs):
    if objs is None:
        return {}
    features = [{'type': 'Feature',
        'geometry': to_shape(o),
        'properties': {'name': name}
    } for o in objs]
    return geojson.dumps(
        {'type': 'FeatureCollection', 'features': features}
    )

# -------- Models ---------------

class Organisation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(128))
    url = db.Column(db.Unicode(255))
    logo = db.Column(db.Unicode(255))

    def __repr__(self):
        return self.name
    def dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'url': self.url,
            'logo': self.logo
        }

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), unique=True)
    created = db.Column(db.DateTime(), default=datetime.datetime.now())
    updated = db.Column(db.DateTime(), default=datetime.datetime.now())
    summary = db.Column(db.Unicode(255))
    details = db.Column(db.UnicodeText)

    status = db.Column(db.String(16), doc="review, labs, collect, present, publish")
    notes = db.Column(db.UnicodeText)

    organisation_id = db.Column(db.Integer, db.ForeignKey(Organisation.id))
    organisation = db.relationship(Organisation,
        backref=db.backref('project', cascade="all, delete-orphan", single_parent=True))

    screenshot = db.Column(db.String(256), doc="Use the Data tab to upload a screenshot")

    is_hidden = db.Column(db.Boolean(), default=False)
    is_featured = db.Column(db.Boolean(), default=False)

    token_edit = db.Column(db.String(64), default=codecs.encode(urandom(12), 'hex').decode())

    def thumb(self, as_thumbnail=True):
        if not self.screenshot: return DEFAULT_THUMB
        name, _ = ospath.splitext(self.screenshot)
        if as_thumbnail:
            return '/screenshots/' + secure_filename('%s_thumb.jpg' % name)
        return '/screenshots/' + secure_filename('%s.jpg' % name)
    def __repr__(self):
        return self.title
    @property
    def url(self):
        return request.host_url.rstrip('/') + url_for('project_page', project_id=self.id)
    @property
    def detail_url(self):
        return request.host_url.rstrip('/') + url_for('project_detail', project_id=self.id)
    def dict(self):
        d = {
            'id': self.id,
            'hidden': self.is_hidden,
            'featured': self.is_featured,
            'name': 'smartuse-%d' % self.id,
            'text': self.title, 'title': self.title,
            'screenshot': self.thumb(False),
            'thumbnail': self.thumb(),
            'date-created': self.created.strftime("%d.%m.%Y"),
            'date-updated': self.updated.strftime("%d.%m.%Y"),
            'status': self.status,
            'summary': self.summary,
            'notes': self.notes,
            'url': self.url,
            'detail_url': self.detail_url,
        }
        if self.organisation:
            d['organisation'] = self.organisation.name
        return d

# Many-to-many relationship
projects_users = db.Table(
    'projects_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('project_id', db.Integer(), db.ForeignKey('project.id'))
)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Unicode(16))
    fullname = db.Column(db.Unicode(128))
    email = db.Column(db.Unicode(128))
    phone = db.Column(db.Unicode(32))
    notes = db.Column(db.UnicodeText)
    biography = db.Column(db.UnicodeText)
    organisation_id = db.Column(db.Integer, db.ForeignKey(Organisation.id))
    organisation = db.relationship(Organisation,
        backref=db.backref('user', cascade="all, delete-orphan", single_parent=True))
    projects = db.relationship(Project, secondary=projects_users,
        backref=db.backref('users', lazy='dynamic'))
    def __repr__(self):
        return self.username
    def gravatar(self):
        gr_size = 80
        if self.email == "": return "/img/usericon.png"
        email = self.email.lower().encode('utf-8')
        gravatar_url = "https://www.gravatar.com/avatar/"
        gravatar_url += hashlib.md5(email).hexdigest() + "?"
        gravatar_url += urlencode({'s':str(gr_size)})
        return gravatar_url
    def dict(self):
        organisation = {}
        if not self.organisation is None:
            organisation = self.organisation.dict()
        return {
            'id': self.id,
            'username': self.username,
            'fullname': self.fullname,
            'gravatar': self.gravatar(),
            'organisation': organisation,
        }

# Many-to-many relationship
projects_resources = db.Table(
    'projects_resources',
    db.Column('project_id', db.Integer(), db.ForeignKey('project.id')),
    db.Column('resource_id', db.Integer(), db.ForeignKey('resource.id'))
)

class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), unique=True)
    description = db.Column(db.UnicodeText)
    notes = db.Column(db.UnicodeText)
    path = db.Column(db.Unicode(256), doc="Use the Data tab to upload files")
    is_embed = db.Column(db.Boolean(), default=False)
    projects = db.relationship('Project', secondary=projects_resources,
        backref=db.backref('resources', lazy='dynamic'))
    # features = db.Column(Geometry("MULTIPOLYGON"))
    def __repr__(self):
        return self.title
    def dict(self):
        content = ''
        notes = ''
        if self.description:
            content = Markup(markdown.markdown(self.description, extensions=MARKDOWN_EXT))
        if self.notes:
            notes = Markup(markdown.markdown(self.notes, extensions=MARKDOWN_EXT))
        r = {
            'id': self.id,
            'name': "smartuse-resource-%d" % self.id,
            'title': self.title,
            'description': content,
            'notes': notes,
            'mediatype': get_media_type(self.path)
        }
        if self.path:
            r['path'] = self.path
        # if self.features is not None:
        #     if not 'data' in r: r['data'] = {}
        #     f = get_features_geojson(r['name'], [self.features])
        #     r['data']['features'] = f
        return r

# ----------- Admin views -----------

UserView = ModelView(User, db.session)
UserView.column_list = ('username', 'fullname', 'organisation')
admin.add_view(UserView)

admin.add_view(ModelView(Organisation, db.session, name="Organisations"))

class ProjectView(ModelView):
    column_list = ('title', 'created', 'updated')
    form_extra_fields = {
        'screenshot': ImageUploadField('Screenshot',
            base_path=screenshot_path, url_relative_path='/screenshots/',
            thumbnail_size=(256, 256, True))
    }
    inline_models = [Resource]
    can_export = True
admin.add_view(ProjectView(Project, db.session, name="Projects (Data Packages)"))

class ResourceView(ModelView):
    column_list = ('title', 'path')
    can_export = True
admin.add_view(ResourceView(Resource, db.session, name="Resources"))

admin.add_view(FileAdmin(upload_path, '/uploads/', name="Data"))

# API views
@app.route("/api/projects", methods=['GET'])
def projects_list():
    return [p.dict() for p in Project.query.filter_by(is_hidden=False,is_featured=False).limit(50).all()]
@app.route("/api/projects/featured", methods=['GET'])
def projects_list_featured():
    return [p.dict() for p in Project.query.filter_by(is_hidden=False,is_featured=True).limit(10).all()]
@app.route("/api/projects/all", methods=['GET'])
def projects_list_all():
    return [p.dict() for p in Project.query.filter_by(is_hidden=False).limit(10).all()]
@app.route("/api/projects/by/<string:BY_TYPE>", methods=['GET'])
def projects_list_by_type(BY_TYPE):
    return [p.dict() for p in Project.query.filter_by(is_hidden=False,status=BY_TYPE).limit(10).all()]

@app.route("/api/resources", methods=['GET'])
def resources_list():
    return [r.dict() for r in Resource.query.limit(10).all()]

@app.route("/api/organisations", methods=['GET'])
def organisations_list():
    return [o.dict() for o in Organisation.query.limit(10).all()]

@app.route("/api/project/<int:project_id>", methods=['GET'])
def project_detail(project_id):
    project = Project.query.filter_by(id=project_id).first_or_404()
    resources = project.resources.order_by(Resource.title).all() # TODO: custom sort
    author = project.users.first()
    if author is not None: author = author.dict()
    return {
        'data': project.dict(),
        'details': project.details,
        'author': author,
        'resources': [r.dict() for r in resources]
    }

def get_file(filename):
    f = open('templates/content/%s' % filename, 'r')
    return f.read()

def get_md(filename):
    t = get_file('%s.md' % filename)
    return Markup(markdown.markdown(t))

# Flask views
@app.route('/about')
def index_about():  return render_template('public/about.pug')
@app.route('/join')
def index_join():   return render_template('public/join.pug')
@app.route('/')
def index_root():
    return render_template('public/browse.pug',
        headline=get_md('home-headline'),
        content=get_file('home-content.html'))
@app.route('/browse')
def index_browse(): return redirect(url_for('index_root'))

@app.route("/project/<int:project_id>")
def project_page(project_id):
    project = Project.query.filter_by(id=project_id).first_or_404()
    content = Markup(markdown.markdown(project.details, extensions=MARKDOWN_EXT))
    meta = project.dict()
    created = arrow.get(meta['date-created'], 'DD.MM.YYYY').humanize()
    updated = arrow.get(meta['date-updated'], 'DD.MM.YYYY').format('DD.MM.YYYY')
    if project.status in project_statuses:
        status = project_statuses[project.status]
        status['class'] = 'fas fa-' + status['icon']
    else:
        status = None
    # version = 1.2
    organisation = project.organisation
    authors = [author.dict() for author in project.users]
    resources = sorted([res.dict() for res in project.resources],
        key=lambda res: res['id'])
    return render_template('public/project.pug', **locals())

# Static paths
@app.route('/img/<path:path>')
def send_static_img(path):
    return send_from_directory('../static/img', path)
@app.route('/scripts/<path:path>')
def send_static_scripts(path):
    return send_from_directory('../static/scripts', path)
@app.route('/styles/<path:path>')
def send_static_styles(path):
    return send_from_directory('../static/styles', path)
@app.route('/tags/<path:path>')
def send_static_tags(path):
    return send_from_directory('../static/tags', path)
@app.route('/vendor/<path:path>')
def send_static_vendor(path):
    return send_from_directory('../static/vendor', path)
@app.route('/meta/<path:path>')
def send_static_meta(path):
    return send_from_directory('../static/meta', path)

@app.route('/theme/<path:path>')
def send_static_theme(path):
    return send_from_directory('../static/theme', path)

@app.route('/data/<path:path>')
def send_static_data(path):
    return send_from_directory('../views/projects', path)
@app.route('/uploads/<path:path>')
def send_uploads(path):
    return send_from_directory('../uploads', path)
@app.route('/screenshots/<path:path>')
def send_screenshots(path):
    return send_from_directory('../screenshots', path)

if __name__ == '__main__':
    db.create_all()
    # Start app
    app.run(debug=True)
