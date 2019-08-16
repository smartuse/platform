FROM python:3.7.1
MAINTAINER SmartUse GmbH "info@smartuse.ch"

ENV LANG 'C.UTF-8'
ENV LC_ALL 'C.UTF-8'

# Create the group and user to be used in this container
RUN groupadd flaskgroup && useradd -m -g flaskgroup -s /bin/bash flask

# Create the working directory (and set it as the working directory)
RUN mkdir -p /opt/app
WORKDIR /opt/app

# Install the package dependencies (this step is separated
# from copying all the source code to avoid having to
# re-install all python packages defined in requirements.txt
# whenever any source code change is made)
COPY requirements.txt /opt/app
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code into the container
COPY . /opt/app

RUN mkdir -p /opt/uploads && chown -Rf flask:flaskgroup /opt/uploads
RUN mkdir -p /opt/screenshots && chown -Rf flask:flaskgroup /opt/screenshots

USER flask
