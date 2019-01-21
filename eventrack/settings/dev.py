from .base import *  # NOQA


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'w+a&o9dl$eu-6ly&q4k2j2l0t8u-v1u)b(4ge#g!gg&3xjm=r7'

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/stable/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'eventrack',
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/stable/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
