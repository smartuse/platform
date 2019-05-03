# SmartUse frontend

A web application for collecting and sharing maps using geospatial Data Packages. Part of SmartUse, a pilot land use mapping project focusing on the greater metropolitan area around Zurich, Switzerland (Metropolitankonferenz Zürich). For more information, see the README in the parent folder, or visit [smartuse.ch](https://smartuse.ch).

Technical details on getting the backend running are in [backend/README](../backend/README.md).

## Usage

To fetch the frontend assets, use npm or [yarn](https://yarnpkg.com/lang/en/) in the root of this repository:

    $ cd smartuse
    $ yarn install

## Docker

Use `docker-compose up -d` to start a daemon, then get a database export, and:

```
sudo docker container exec -u postgres -i smartuse_postgres_1 createdb smartuse
sudo docker container exec -u postgres -i smartuse_postgres_1 psql < ../my-backup.sql
```

## License

MIT - details in [LICENSE](../LICENSE) file.
