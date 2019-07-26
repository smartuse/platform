web: gunicorn app:app -b 0.0.0.0:$PORT -w 3 --log-file=-
init: flask db upgrade
