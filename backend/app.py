from flask import Flask, Markup
from flask import (
    url_for,
    request,
    render_template,
    send_from_directory
)
from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import flask_admin as admin
from flask_admin.model import BaseModelView
from flask_admin.contrib.geoa import ModelView
from flask_admin.contrib.fileadmin import FileAdmin

# Geoshapes in model
from geoalchemy2.types import Geometry
from geoalchemy2.shape import to_shape
import geojson, markdown

# Gravatar
from urllib.parse import urlencode
import hashlib
import os.path as ospath

# Locals
from .util import *

# Create application
app = FlaskAPI(__name__, static_url_path='')
app.debug = True
app.config.from_pyfile('config.py')
app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Create admin
admin = admin.Admin(app, name='SmartUse', template_mode='bootstrap3')
login_manager = LoginManager()
login_manager.init_app(app)

# Define tables and models
projects_users = db.Table(
    'projects_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('project_id', db.Integer(), db.ForeignKey('project.id'))
)

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
    created = db.Column(db.DateTime())
    updated = db.Column(db.DateTime())
    summary = db.Column(db.Unicode(255))
    details = db.Column(db.UnicodeText)

    column_exclude_list = ('summary', 'details')

    def __repr__(self):
        return self.title
    def dict(self):
        return {
            'id': self.id,
            'name': 'smartuse-%d' % self.id,
            'text': self.title,
            'title': self.title,
            'date-created': self.created.strftime("%Y-%d-%m"),
            'date-updated': self.updated.strftime("%Y-%d-%m"),
            'summary': self.summary,
            'detail_url': request.host_url.rstrip('/') + url_for('project_detail', project_id=self.id),
        }

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Unicode(16))
    fullname = db.Column(db.Unicode(128))
    email = db.Column(db.Unicode(128))
    phone = db.Column(db.Unicode(32))
    notes = db.Column(db.UnicodeText)
    organisation_id = db.Column(db.Integer, db.ForeignKey(Organisation.id))
    organisation = db.relationship(Organisation, backref=db.backref('user', cascade="all, delete-orphan", single_parent=True))
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
        return {
            'id': self.id,
            'username': self.username,
            'fullname': self.fullname,
            'gravatar': self.gravatar(),
            'organisation': self.organisation.dict(),
        }

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)
    
projects_resources = db.Table(
    'projects_resources',
    db.Column('project_id', db.Integer(), db.ForeignKey('project.id')),
    db.Column('resource_id', db.Integer(), db.ForeignKey('resource.id'))
)
SUPPORTED_FORMATS = (
    'png', 'jpg', 'geojson', 'datapackage', 'embed'
)

class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), unique=True)
    description = db.Column(db.UnicodeText)
    path = db.Column(db.Unicode(256), doc="Use the Data tab to upload files")
    dataformat = db.Column(db.Enum(*SUPPORTED_FORMATS, name="dataformats"))
    projects = db.relationship('Project', secondary=projects_resources,
        backref=db.backref('resources', lazy='dynamic'))
    # features = db.Column(Geometry("MULTIPOLYGON"))
    def __repr__(self):
        return self.title
    def dict(self):
        r = {
            'id': self.id,
            'name': "smartuse-resource-%d" % self.id,
            'title': self.title,
            'description': self.description,
            'dataformat': self.dataformat,
            'mediatype': get_media_type(self.dataformat)
        }
        if self.path:
            r['path'] = self.path
        # if self.features is not None:
        #     if not 'data' in r: r['data'] = {}
        #     f = get_features_geojson(r['name'], [self.features])
        #     r['data']['features'] = f
        return r

# Add views
ResourceView = ModelView(Resource, db.session)
ResourceView.column_list = ['title', 'dataformat', 'projects']
admin.add_view(ResourceView)

ProjectView = ModelView(Project, db.session)
ProjectView.column_list = ('title', 'created', 'updated')
admin.add_view(ProjectView)

UserView = ModelView(User, db.session)
UserView.column_list = ('username', 'fullname', 'organisation')
admin.add_view(UserView)

admin.add_view(ModelView(Organisation, db.session))

# Upload views
upload_path = ospath.join(ospath.dirname(__file__), '..', 'uploads')
admin.add_view(FileAdmin(upload_path, '/uploads/', name="Data"))

# API views
@app.route("/api/projects", methods=['GET'])
def projects_list():
    return [p.dict() for p in Project.query.limit(10).all()]

@app.route("/api/resources", methods=['GET'])
def resources_list():
    return [r.dict() for r in Resource.query.limit(10).all()]

@app.route("/api/project/<int:project_id>", methods=['GET'])
def project_detail(project_id):
    project = Project.query.filter_by(id=project_id).first_or_404()
    resources = project.resources.order_by(Resource.title).all() # TODO: custom sort
    return {
        'data': project.dict(),
        'details': project.details,
        'author': project.users.first().dict(),
        'resources': [r.dict() for r in resources]
    }

# Flask views
@app.route('/')
def index():
    f = open('templates/public/index.md', 'r')
    content = Markup(markdown.markdown(f.read()))
    projects = Project.query.all()
    meta = { 'title': 'Home' }
    return render_template('public/home.pug', **locals())

@app.route("/project/<int:project_id>")
def project_page(project_id):
    project = Project.query.filter_by(id=project_id).first_or_404()
    content = Markup(markdown.markdown(project.details))
    meta = project.dict()
    author = project.users.first().dict()
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
@app.route('/data/<path:path>')
def send_static_data(path):
    return send_from_directory('../views/projects', path)
@app.route('/uploads/<path:path>')
def send_uploads(path):
    return send_from_directory('../uploads', path)

if __name__ == '__main__':
    db.create_all()
    # Start app
    app.run(debug=True)
