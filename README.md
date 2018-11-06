[![Build Status](https://travis-ci.org/FedorSelitsky/eventrack.svg?branch=master)](https://travis-ci.org/FedorSelitsky/eventrack)

# Eventrack

[![Eventrack logo](https://github.com/FedorSelitsky/eventrack/blob/master/event/static/event/images/logo.png)](http://eventrack.org/)

[Eventrack](http://eventrack.org/) is a concert tracking application. Eventrack allows users to track their favorite artists and discover concerts. It also allows users to submit events, contributing to archives of upcoming and past shows. Users can bookmark their favorite artists and receive recommendations about their upcoming events.

## Requirements

* Python 3.7.1
* Django 2.1.3
* Channels 2.1.5
* Psycopg 2.7.5
* PostgreSQL 10.5

## Getting started

* Create a virtual environment with interpreter `Python 3.7`.
* Create a database named `eventrack`.
* Run `pip install -r requirements.txt` to install dependencies.
* Run `export DJANGO_SETTINGS_MODULE=eventrack.settings.dev` to set the environment variable.
* Run `python manage.py migrate` to apply migrations.
* Run `python manage.py runserver` to run the app and view it on http://localhost:8000/
