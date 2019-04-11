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
from sqlalchemy import or_, desc

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

from . import helper

# Create application
app = FlaskAPI(__name__, static_url_path='')
app.debug = True
app.config.from_pyfile('config.py')
app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Various presets
with open(ospath.join(ospath.dirname(__file__), 'templates','presets','project-categories.json'), "r") as f:
    project_categories = json.load(f)
screenshot_path = ospath.join(ospath.dirname(__file__), '..', 'screenshots')
upload_path = ospath.join(ospath.dirname(__file__), '..', 'uploads')
DEFAULT_THUMB = '../img/usermap.jpg'

# Create admin
admin = admin.Admin(app, name='SmartUse', template_mode='bootstrap3')

# -------- Models ---------------

class Organisation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(128), nullable=False)
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

class License(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Unicode(256), unique=True, nullable=False)
    name = db.Column(db.Unicode(256), unique=True, nullable=False, doc="Short, lowercase identifer")
    path = db.Column(db.Unicode(2048), doc="Enter URL to the license")
    def __repr__(self):
        return self.title
    def dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'title': self.title,
            'path': self.path or '',
        }

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), unique=True, nullable=False)
    created = db.Column(db.DateTime(), default=datetime.datetime.now())
    updated = db.Column(db.DateTime(), default=datetime.datetime.now())
    summary = db.Column(db.Unicode(255))
    details = db.Column(db.UnicodeText)
    category = db.Column(db.String(32), doc="review, labs, collect, present, publish")

    organisation_id = db.Column(db.Integer, db.ForeignKey(Organisation.id))
    organisation = db.relationship(Organisation,
        backref=db.backref('project', cascade="all, delete-orphan", single_parent=True))

    license_id = db.Column(db.Integer, db.ForeignKey(License.id))
    license = db.relationship(License,
        backref=db.backref('project', cascade="all, delete-orphan", single_parent=True))

    screenshot = db.Column(db.String(256), doc="Use the Data tab to upload a screenshot")

    is_hidden = db.Column(db.Boolean(), default=False)
    is_featured = db.Column(db.Boolean(), default=False)

    slug = db.Column(db.String(64), unique=True)
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
        return request.host_url.rstrip('/') + url_for('project_page_by_slug', project_slug=self.slug)
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
            'summary': self.summary,
            'url': self.url,
            'path': self.detail_url,
            'mediatype': "application/vnd.datapackage+json",
            'format': helper.media_name('datapackage.json'),
        }
        if self.category:
            d['category'] = self.category
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
    username = db.Column(db.Unicode(16), nullable=False)
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
        d = {
            'id': self.id,
            'username': self.username,
            'fullname': self.fullname,
            'gravatar': self.gravatar(),
        }
        if not self.organisation is None:
            d['organisation'] = self.organisation.dict()
        return d

class Source(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Unicode(256), unique=True, nullable=False)
    path = db.Column(db.Unicode(2048), doc="Enter URL to the data source")
    fmt = db.Column(db.String(32))
    organisation_id = db.Column(db.Integer, db.ForeignKey(Organisation.id))
    organisation = db.relationship(Organisation,
        backref=db.backref('source', cascade="all, delete-orphan", single_parent=True))
    def __repr__(self):
        return self.title
    def dict(self):
        d = {
            'id': self.id,
            'title': self.title,
            'path': self.path or '',
            'format': helper.media_name(self.path, self.fmt),
            'mediatype': helper.media_mime(self.path, self.fmt),
        }
        if not self.organisation is None:
            d['organisation'] = self.organisation.dict()
        return d

# Many-to-many relationship
projects_renderings = db.Table(
    'projects_renderings',
    db.Column('project_id',   db.Integer(), db.ForeignKey('project.id')),
    db.Column('rendering_id', db.Integer(), db.ForeignKey('rendering.id'))
)
sources_renderings = db.Table(
    'sources_renderings',
    db.Column('source_id',    db.Integer(), db.ForeignKey('source.id')),
    db.Column('rendering_id', db.Integer(), db.ForeignKey('rendering.id'))
)

class Rendering(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order = db.Column(db.Integer)
    title = db.Column(db.String(128), unique=True, nullable=False)
    description = db.Column(db.UnicodeText)
    path = db.Column(db.Unicode(2048),
        doc="Provide a URL here, use the Data tab to upload files")
    projects = db.relationship('Project', secondary=projects_renderings,
        backref=db.backref('renderings', lazy='dynamic'))
    sources = db.relationship('Source', secondary=sources_renderings,
        backref=db.backref('renderings', lazy='dynamic'))
    def __repr__(self):
        return self.title
    def dict(self):
        content = ''
        if self.description:
            try:
                content = Markup(markdown.markdown(self.description, extensions=MARKDOWN_EXT))
            except Exception as e:
                print(e)
        return {
            'id': self.id,
            'title': self.title,
            'name': helper.slugify(self.title),
            'description': content,
            'mediatype': helper.media_mime(self.path),
            'format': helper.media_name(self.path),
            'path': self.path or '',
            'sources': [r.dict() for r in self.sources]
        }

# ----------- Admin views -----------

UserView = ModelView(User, db.session, name="Users")
UserView.column_list = ('username', 'fullname', 'organisation')
admin.add_view(UserView)

admin.add_view(ModelView(Organisation, db.session, name="Organisations"))

class ProjectView(ModelView):
    column_list = ('title', 'created', 'updated', 'category')
    form_excluded_columns = ('slug', 'token_edit')
    form_extra_fields = {
        'screenshot': ImageUploadField('Screenshot',
            base_path=screenshot_path, url_relative_path='/screenshots/',
            thumbnail_size=(256, 256, True))
    }
    inline_models = [Rendering]
    can_export = True
    def on_model_change(view, form, model, is_created):
        model.slug = helper.slugify(form.title.data)

admin.add_view(ProjectView(Project, db.session, name="Projects (Data Packages)"))

class RenderingView(ModelView):
    column_list = ('title', 'path')
    can_export = True
admin.add_view(RenderingView(Rendering, db.session, name="Renderings (Views)"))

admin.add_view(ModelView(Source, db.session, name="Data sources"))

admin.add_view(ModelView(License, db.session, name="Licenses"))

admin.add_view(FileAdmin(upload_path, '/uploads/', name="Uploads"))

# API views
@app.route("/api/projects", methods=['GET'])
def projects_list():
    return [p.dict() for p in Project.query
        .filter_by(is_hidden=False,is_featured=False)
        .limit(50).all()]

@app.route("/api/projects/featured", methods=['GET'])
def projects_list_featured():
    return [p.dict() for p in Project.query
        .filter_by(is_hidden=False,is_featured=True)
        .limit(10).all()]

@app.route("/api/projects/all", methods=['GET'])
def projects_list_all():
    return [p.dict() for p in Project.query
        .filter_by(is_hidden=False)
        .order_by(Project.category)
        .limit(25).all()]

@app.route("/api/projects/by/<string:BY_CAT>", methods=['GET'])
def projects_list_by_category(BY_CAT):
    return [p.dict() for p in Project.query
        .filter_by(is_hidden=False,category=BY_CAT)
        .limit(10).all()]

@app.route('/api/projects/search', methods=['GET'])
def projects_search():
    q = request.args.get('q')
    if not q or len(q.strip()) < 3: return []
    q = '%' + q.strip() + '%'
    return [p.dict() for p in Project.query.filter(or_(
        Project.title.ilike(q),
        Project.details.ilike(q),
        Project.summary.ilike(q),
    )).limit(50).all()]

@app.route("/api/organisations", methods=['GET'])
def organisations_list():
    return [o.dict() for o in Organisation.query.limit(10).all()]

@app.route("/api/project/<int:project_id>", methods=['GET'])
def project_detail(project_id):
    project = Project.query.filter_by(id=project_id).first_or_404()
    renderings = project.renderings.order_by(Rendering.order).all()
    d = {
        'data': project.dict(),
        'details': project.details,
        'renderings': [r.dict() for r in renderings],
    }
    author = project.users.first()
    if author is not None: d['author'] = author.dict()
    license = project.license
    if license is not None: d['license'] = license.dict()
    return d

def get_file(filename):
    f = open(ospath.join(
            ospath.dirname(__file__),
            'templates',
            'content',
            filename
        ), 'r')
    return f.read()

def get_md(filename):
    t = get_file('%s.md' % filename)
    return Markup(markdown.markdown(t))

# Flask views
@app.route('/about')
def index_about():
    return render_template('public/about.pug', content=get_md('about-page'))

# @app.route('/join')
# def index_join():   return render_template('public/join.pug')

@app.route('/search')
def index_search():
    return render_template('public/search.pug')

@app.route('/')
def index_root():
    return render_template('public/home.pug',
        headline=get_md('home-headline'),
        bottom=get_file('home-bottom.html'),
        about=get_md('home-about'),
    )

@app.route("/project/<project_slug>")
def project_page_by_slug(project_slug):
    return project_page(Project.query.filter_by(slug=project_slug).first_or_404())

@app.route("/project/<int:project_id>")
def project_page_by_id(project_id):
    return project_page(Project.query.filter_by(id=project_id).first_or_404())

def project_page(project):
    content = Markup(markdown.markdown(project.details, extensions=MARKDOWN_EXT))
    meta = project.dict()
    created = arrow.get(meta['date-created'], 'DD.MM.YYYY').humanize()
    updated = arrow.get(meta['date-updated'], 'DD.MM.YYYY').format('DD.MM.YYYY')
    category = None
    if project.category in project_categories:
        category = project_categories[project.category]
        category['class'] = 'fas fa-' + category['icon']
    # version = 1.2
    organisation = project.organisation
    authors = [author.dict() for author in project.users]
    renderings = sorted([res.dict() for res in project.renderings],
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
@app.route('/screenshots/<path:path>')
def send_screenshots(path):
    return send_from_directory('../screenshots', path)

@app.route('/data/<path:path>')
def send_static_data(path):
    return send_from_directory('../views/projects', path)
@app.route('/uploads/<path:path>')
def send_uploads(path):
    return send_from_directory('../uploads', path)
@app.route('/api/project/<int:pid>/<path:path>')
def send_uploads_project(pid, path):
    return send_from_directory('../uploads', path)

if __name__ == '__main__':
    db.create_all()
    # Start app
    app.run(debug=True)
