from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['CFG_SECRET_KEY']

ALLOWED_HOSTS = os.environ['CFG_ALLOWED_HOSTS'].split(',')


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.postgresql',
        'NAME':     os.environ['CFG_DATABASES_NAME'],
        'USER':     os.environ['CFG_DATABASES_USER'],
        'PASSWORD': os.environ['CFG_DATABASES_PASSWORD'],
        'HOST':     os.environ['CFG_DATABASES_HOST'],
        'PORT':     os.environ['CFG_DATABASES_PORT'],
    }
}
