from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_api import FlaskAPI

import flask_admin as admin
from flask_admin.contrib.geoa import ModelView
from geoalchemy2.types import Geometry
from geoalchemy2.shape import to_shape
import geojson

# Create application
app = FlaskAPI(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

# Create admin
admin = admin.Admin(app, name='SmartUse', template_mode='bootstrap3')

# Define tables and models
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
    organisation = db.Column(db.Unicode(128))
    notes = db.Column(db.UnicodeText)
    projects = db.relationship('Project', secondary=projects_users,
        backref=db.backref('users', lazy='dynamic'))
    def __repr__(self):
        return self.username

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), unique=True)
    created = db.Column(db.DateTime())
    updated = db.Column(db.DateTime())
    summary = db.Column(db.Unicode(255))
    details = db.Column(db.UnicodeText)
    def __repr__(self):
        return self.title
    def dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'created': self.created,
            'updated': self.updated,
            'summary': self.summary,
            'details': self.details
        }

projects_resources = db.Table(
    'projects_resources',
    db.Column('project_id', db.Integer(), db.ForeignKey('project.id')),
    db.Column('resource_id', db.Integer(), db.ForeignKey('resource.id'))
)

SUPPORTED_FORMATS = (
    'png', 'jpg', 'geojson'
)

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

class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    description = db.Column(db.UnicodeText)
    path = db.Column(db.Unicode(256))
    dataformat = db.Column(db.Enum(*SUPPORTED_FORMATS, name="dataformats"))
    projects = db.relationship('Project', secondary=projects_resources,
        backref=db.backref('resources', lazy='dynamic'))
    center = db.Column(Geometry("POINT"))
    zoom = db.Column(db.Integer)
    features = db.Column(Geometry("MULTIPOLYGON"))
    def __repr__(self):
        return self.name
    def dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'path': self.path,
            'dataformat': self.dataformat,
            'zoom': self.zoom,
            'center': get_features_geojson(self.name + ' center', [self.center]),
            'features': get_features_geojson(self.name, [self.features]),
        }

# Add views
admin.add_view(ModelView(User, db.session, category='Users'))
admin.add_view(ModelView(Resource, db.session, category='Datasets'))
admin.add_view(ModelView(Project, db.session, category='Projects'))

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
    return {
        'data': project.dict(),
        'resources': [r.dict() for r in project.resources.all()]
    }

# Flask views
@app.route('/')
def index():
    return '<a href="/admin/">Admin access</a>'

if __name__ == '__main__':
    db.create_all()
    # Start app
    app.run(debug=True)
