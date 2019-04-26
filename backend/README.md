# SmartUse backend

A web application for collecting and sharing maps using geospatial Data Packages. Part of SmartUse, a pilot land use mapping project focusing on the greater metropolitan area around Zurich, Switzerland (Metropolitankonferenz Zürich). For more information, see the README in the parent folder, or visit [smartuse.ch](https://smartuse.ch).

Technical details on getting the backend running follow. See also details on updating the frontend in the [static README](../static/README.md).

## Usage

Get a hold of **Python 3** and [Pipenv](https://github.com/pypa/pipenv) on your machine.

    $ git clone https://gitlab.com/smartuse/smartuse.git
    $ git submodule init
    $ git submodule foreach git pull

To install dependencies, use pip or [pipenv](https://github.com/pypa/pipenv):

    $ mkdir smartuse/uploads
    $ cd smartuse/backend
    $ pipenv --three
    $ pipenv install

Configure your **PostgreSQL** database, and [Mapbox](https://www.mapbox.com/help/how-access-tokens-work/) access tokens to render GeoJSON:

    $ export DATABASE_URI="postgresql+psycopg2://user:password@127.0.0.1/smartuse"
    $ export SECRET_KEY="12345"
    $ export MAPBOX_ID="abcd.1234"
    $ export MAPBOX_TOKEN="pk.abcd.1234"

To initialize and/or migrate the database:

    $ flask db init
    $ flask db migrate
    $ flask db upgrade

To start the backend:

    $ export FLASK_ENV=development
    $ export FLASK_DEBUG=1
    $ export FLASK_APP=app.py
    $ flask run

The app will now be available at http://localhost:5000

## License

MIT - details in [LICENSE](../LICENSE) file.
