import os

from celery.schedules import crontab

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.postgres',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'artist.apps.ArtistConfig',
    'event.apps.EventConfig',
    'venue.apps.VenueConfig',
    'user.apps.UserConfig',
    'channels',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'eventrack.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'eventrack.wsgi.application'


# User model
# https://docs.djangoproject.com/en/stable/ref/settings/#auth-user-model

AUTH_USER_MODEL = 'user.User'


# Password validation
# https://docs.djangoproject.com/en/stable/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Login URL
# https://docs.djangoproject.com/en/stable/ref/settings/#login-url

LOGIN_URL = 'user:signin'


# Internationalization
# https://docs.djangoproject.com/en/stable/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Minsk'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Logging
# https://docs.djangoproject.com/en/stable/topics/logging/#configuring-logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'verbose': '[%(asctime)s] (%(process)d/%(thread)d) %(name)s %(levelname)s: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        },
    },
    'root': {
        'handlers': ['mail_admins', 'console'],
        'level': 'ERROR',
        'formatter': 'verbose',
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins', 'console'],
            'level': 'ERROR',
            'propagate': False,
            'formatter': 'verbose',
        },
        'django.security': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
            'formatter': 'verbose',
        },
    },
}


# ASGI
# https://channels.readthedocs.io/en/stable/deploying.html#configuring-the-asgi-application
ASGI_APPLICATION = 'eventrack.routing.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [os.getenv('REDIS_HOST', 'redis://localhost:6379')],
        },
    }
}


# Artists count
ARTISTS_COUNT = 5


# Celery
# http://docs.celeryproject.org/en/stable/userguide/configuration.html
CELERY_TIMEZONE = TIME_ZONE
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CELERY_BEAT_SCHEDULE = {
    'fetch_artists': {
        'task': 'artist.tasks.fetch_artists',
        'schedule': crontab(minute=0, hour=0),
    },
    'update_artists': {
        'task': 'artist.tasks.update_artists',
        'schedule': crontab(minute=0, hour='*/1'),
    },
    'fetch_events': {
        'task': 'event.tasks.fetch_events',
        'schedule': crontab(minute=0, hour='*/12'),
    },
}


# Songkick API
# https://www.songkick.com/developer
SONGKICK_API_KEY = os.getenv('SONGKICK_API_KEY', 'YOUR_API_KEY')


# Bandsintown API
# https://app.swaggerhub.com/apis/Bandsintown/PublicAPI/3.0.0
BANDSINTOWN_APP_ID = os.getenv('BANDSINTOWN_APP_ID', 'YOUR_APP_ID')
