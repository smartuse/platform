## SmartUse

A land use mapping project focusing on the greater metropolitan area around Zurich, Switzerland (Metropolitankonferenz Zürich).

## Usage

Get a hold of **Python 3** and [Pipenv](https://github.com/pypa/pipenv) on your machine.

    $ git clone https://gitlab.com/smartuse/smartuse.git

To fetch the frontend assets, use npm or [yarn](https://yarnpkg.com/lang/en/):

    $ cd smartuse
    $ yarn install

To install and start the backend:

    $ cd smartuse/backend
    $ pipenv --three
    $ pipenv install
    $ python app.py

The app will now be available at http://localhost:5000

The splash page is at `static/splashpage/index.html`, to preview it:

    $ cd smartuse/static
    $ python -m http.server

## License

MIT - details in [LICENSE](LICENSE) file.
