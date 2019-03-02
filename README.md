[![Build Status](https://travis-ci.org/FedorSelitsky/eventrack.svg?branch=master)](https://travis-ci.org/FedorSelitsky/eventrack)

# Eventrack

[![Eventrack logo](https://github.com/FedorSelitsky/eventrack/blob/master/event/static/event/images/logo.png)](https://eventrack.org/)

[Eventrack](https://eventrack.org/) is a concert tracking application. Eventrack allows users to track their favorite artists and discover concerts.  
Users can bookmark their favorite artists and receive recommendations about their upcoming events.

## Requirements

* Python 3.7.2
* Django 2.1.7
* Django REST Framework 3.9.1
* Channels 2.1.7
* PostgreSQL 10.6

## Getting started

* Create a virtual environment with interpreter `Python 3.7`.
* Create a database named `eventrack`.
* Run `CREATE EXTENSION postgis` to enable spatial functionality.
* Run `pip install -r requirements.txt` to install dependencies.
* Run `export DJANGO_SETTINGS_MODULE=eventrack.settings.dev` to set the environment variable.
* Run `python manage.py migrate` to apply migrations.
* Run `python manage.py runserver` to run the app and view it on http://localhost:8000/

## Monitoring and administrating

* Run `flower --port=5555` to launch the server and open http://localhost:5555/
