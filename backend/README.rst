SQLAlchemy model backend integration

1. Create and activate a virtual environment

    pyvenv env
    . env/bin/activate

2. Install requirements

    pip install -r requirements.txt

3. Setup the database

    psql postgres

    CREATE DATABASE smartuse_geo;
    CREATE ROLE smartuse_geo LOGIN PASSWORD 'smartuse_geo';
    GRANT ALL PRIVILEGES ON DATABASE smartuse_geo TO smartuse_geo;
    \q

    psql smartuse_geo

    CREATE EXTENSION postgis;
    \q

4. Configure base maps

Register for a free account at `Mapbox <https://www.mapbox.com/>`_ and set
the *MAPBOX_MAP_ID* and *MAPBOX_ACCESS_TOKEN* config variables accordingly.

5. Run the application

    python app.py
