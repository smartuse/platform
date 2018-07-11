import os

SECRET_KEY = 'This is an INSECURE secret!! DO NOT use this in production!!'
if 'SECRET_KEY' in os.environ:
    SECRET_KEY = os.environ['SECRET_KEY']

# database connection
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
if 'DATABASE_URI' in os.environ:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URI']

# credentials for loading map tiles from mapbox
MAPBOX_MAP_ID = os.environ['MAPBOX_ID']
MAPBOX_ACCESS_TOKEN = os.environ['MAPBOX_TOKEN']
