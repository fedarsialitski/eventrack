import dj_database_url

from .base import *  # NOQA


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
if 'CFG_SECRET_KEY' in os.environ:
    SECRET_KEY = os.environ['CFG_SECRET_KEY']

if 'CFG_ALLOWED_HOSTS' in os.environ:
    ALLOWED_HOSTS = os.environ['CFG_ALLOWED_HOSTS'].split(',')


# Database
# https://docs.djangoproject.com/en/stable/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(
        default='postgis://postgis:postgis@postgis/postgis',
    ),
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/stable/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.getenv('CFG_STATIC_ROOT', os.path.join(BASE_DIR, 'static'))

MEDIA_URL = '/media/'
MEDIA_ROOT = os.getenv('CFG_MEDIA_ROOT', os.path.join(BASE_DIR, 'media'))


# ManifestStaticFilesStorage
# https://docs.djangoproject.com/en/stable/ref/contrib/staticfiles/#manifeststaticfilesstorage

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
