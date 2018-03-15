from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import flask_admin as admin
from geoalchemy2.types import Geometry
from flask_admin.contrib.geoa import ModelView

# Create application
app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

# Flask views
@app.route('/')
def index():
    return '<a href="/admin/">Admin access</a>'

# Create admin
admin = admin.Admin(app, name='SmartUse', template_mode='bootstrap3')

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
    def __unicode__(self):
        return self.username

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), unique=True)
    created = db.Column(db.DateTime())
    updated = db.Column(db.DateTime())
    summary = db.Column(db.Unicode(255))
    details = db.Column(db.UnicodeText)
    def __unicode__(self):
        return self.title

projects_resources = db.Table(
    'projects_resources',
    db.Column('project_id', db.Integer(), db.ForeignKey('project.id')),
    db.Column('resource_id', db.Integer(), db.ForeignKey('resource.id'))
)

SUPPORTED_FORMATS = (
    'png', 'jpg', 'geojson'
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

# Add views
admin.add_view(ModelView(User, db.session, category='Users'))
admin.add_view(ModelView(Resource, db.session, category='Datasets'))
admin.add_view(ModelView(Project, db.session, category='Projects'))

if __name__ == '__main__':

    db.create_all()

    # Start app
    app.run(debug=True)
