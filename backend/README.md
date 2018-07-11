## SmartUse

A land use mapping project focusing on the greater metropolitan area around Zurich, Switzerland (Metropolitankonferenz Zürich).

## Usage

Get a hold of **Python 3** and [Pipenv](https://github.com/pypa/pipenv) on your machine.

    $ git clone https://gitlab.com/smartuse/smartuse.git

To fetch the frontend assets, use npm or [yarn](https://yarnpkg.com/lang/en/):

    $ cd smartuse
    $ yarn install

To install dependencies, use pip or [pipenv](https://github.com/pypa/pipenv):

    $ cd smartuse/backend
    $ pipenv --three
    $ pipenv install

If you would like to use a local Postgres database, enable development mode:

    $ export FLASK_DEBUG=1

To initialize and/or migrate the database:

    $ flask db init
    $ flask db migrate
    $ flask db upgrade

To start the backend:

    $ export FLASK_APP=app.py
    $ export FLASK_ENV=development
    $ flask run

The app will now be available at http://localhost:5000

## Static files

The splash page is at `static/splashpage/index.html`, to preview it:

    $ cd smartuse/static
    $ python -m http.server

## License

MIT - details in [LICENSE](LICENSE) file.
