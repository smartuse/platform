# Create dummy secrey key so we can use sessions
SECRET_KEY = 'd578a8c9b30e'

# database connection
SQLALCHEMY_DATABASE_URI = 'postgres://fjmehnha:FJimrMverMOxHvqZj8tPRA-P5MCVnUde@dumbo.db.elephantsql.com:5432/fjmehnha'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# development settings
import os
if 'FLASK_DEBUG' in os.environ and os.environ['FLASK_DEBUG']:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://oleg:smartuse@127.0.0.1/smartuse'
    SQLALCHEMY_ECHO = False

# credentials for loading map tiles from mapbox
MAPBOX_MAP_ID = 'petrusjvr.mbhn4pjj'
MAPBOX_ACCESS_TOKEN = 'pk.eyJ1Ijoic21hcnR1c2UiLCJhIjoiY2pkNGowcGdzMHhpbzMzcWp3eGYydGhmMiJ9.k9QyYo-2pFvyyFDJiz16UA'
