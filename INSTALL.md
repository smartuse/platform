# Smart Use backend

A web application for collecting and sharing maps powered by a Geospatial Data Package API. Part of Smart Use, a pilot land use mapping project focusing on the greater metropolitan area around Zurich, Switzerland. For more information, see the main [README](README.md). Details on updating the frontend can be found in the [static README](static/README.md).

Technical details on getting the backend service running follow.

## Usage

See also [Docker instructions](#Docker) below.

Get a hold of **Python 3** and [Pipenv](https://github.com/pypa/pipenv) on your machine.

    $ git clone https://github.com/smartuse/platform.git smartuse

To install dependencies, use pip or [pipenv](https://github.com/pypa/pipenv):

    $ cd smartuse
    $ mkdir uploads
    $ cd backend
    $ pipenv --three

At this point you will have a virtual environment, which you can activate with:

    $ pipenv shell

You'll also need to install dependencies with:

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

## Docker

1) Copy `.env.example` to `.env` in the root path and modify with your preferred settings.

2) Run `docker-compose build` in the root folder and make sure you don't get any errors.

3) Use `docker-compose up -d` to start a daemon

4) Create a database:

```
sudo docker container exec -u postgres -i platform_postgres_1 createdb smartuse
```

If you have a database export, you should:

```
sudo docker container exec -u postgres -i platform_postgres_1 psql < my-backup.sql
```

If not, then:

```
sudo docker-compose exec web flask db upgrade
```

## Production

In production we use gunicorn + nginx + pipenv, monitored by this supervisor script:

```
[program:smartuse]
directory=/srv/smartuse-platform/backend
command=pipenv run gunicorn app:app -b 0.0.0.0:5555 -w 3
autostart=true
autorestart=true
user=smartuser
stderr_logfile=/var/log/smartuse/smartuse.err.log
stdout_logfile=/var/log/smartuse/smartuse.out.log
environment=
    FLASK_APP="app.py",
    SECRET_KEY="...",
    DATABASE_URI="postgres://..",
    MAPBOX_ID="..",
    MAPBOX_TOKEN=".."
```

## License

MIT - details in [LICENSE](LICENSE) file.
