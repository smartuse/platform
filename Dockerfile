FROM ubuntu:latest
MAINTAINER Fabien Schwob "fabien.schwob@89grad.ch"

ENV LANG 'C.UTF-8'
ENV LC_ALL 'C.UTF-8'
ENV FLASK_DEBUG  1
ENV MAPBOX_ID "121212122"
ENV MAPBOX_TOKEN = "34567890"
ENV SQLALCHEMY_DATABASE_URI = "postgis://exqmple.com/db"

RUN apt-get update -y 
RUN apt-get install -y apt-utils python3-pip python3-dev build-essential
RUN pip3 install pipenv

COPY backend/ /app
WORKDIR /app

RUN mkdir uploads

RUN pipenv install


CMD ["pipenv", "run", "python3", "app.py"]