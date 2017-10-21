from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
if 'CFG_SECRET_KEY' in os.environ:
    SECRET_KEY = os.environ['CFG_SECRET_KEY']

if 'CFG_ALLOWED_HOSTS' in os.environ:
    ALLOWED_HOSTS = os.environ['CFG_ALLOWED_HOSTS'].split(',')


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.postgresql',
        'NAME':     os.environ.get('CFG_DATABASES_NAME',     'postgres'),
        'USER':     os.environ.get('CFG_DATABASES_USER',     'postgres'),
        'PASSWORD': os.environ.get('CFG_DATABASES_PASSWORD', 'postgres'),
        'HOST':     os.environ.get('CFG_DATABASES_HOST',     'postgres'),
        'PORT':     os.environ.get('CFG_DATABASES_PORT',     '5432'),
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.environ.get('CFG_STATIC_ROOT', os.path.join(BASE_DIR, 'static'))

MEDIA_URL = '/media/'
MEDIA_ROOT = os.environ.get('CFG_MEDIA_ROOT', os.path.join(BASE_DIR, 'media'))
