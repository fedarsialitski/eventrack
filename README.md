# [Eventrack](http://eventrack.org/)

[![Eventrack logo](https://github.com/FedorSelitsky/eventrack/blob/master/event/static/event/images/logo.png)](http://eventrack.org/)

[Eventrack](http://eventrack.org/) is a concert tracking application. Eventrack allows users to track their favorite artists and discover concerts. It also allows users to submit events, contributing to archives of upcoming and past shows. Users can bookmark their favorite artists and receive recommendations about their upcoming events.

## Requirements

* Python 3.6.2
* Django 1.11.3
* Psycopg 2.7.3
* PostgreSQL 9.6.5

## Getting started

* Create a virtual environment with interpreter `Python 3.6`.
* Create a database named `eventrack`.
* Run `pip install -r requirements.txt` to install dependencies.
* Run `export DJANGO_SETTINGS_MODULE=eventrack.settings.dev` to set the environment variable.
* Run `python manage.py migrate` to apply migrations.
* Run `python manage.py runserver` to run the app and view it on http://localhost:8000/
