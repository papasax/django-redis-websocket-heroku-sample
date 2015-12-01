# Django settings for unit test project.
import os
import dj_redis_url
import dj_database_url
from os.path import join, dirname
from dotenv import load_dotenv

# Absolute path to the directory that holds static files.
# Example: "/home/media/media.lawrence.com/static/"
SETTINGS_DIR = os.path.dirname(__file__)
PROJECT_DIR = os.path.abspath(os.path.join(SETTINGS_DIR, os.pardir))

dotenv_path = join(PROJECT_DIR, '.env')
load_dotenv(dotenv_path)

try:
    DEBUG = os.environ['DEBUG']
except:
    DEBUG = False

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:////{0}'.format(os.path.join(PROJECT_DIR, 'db.sqlite3'))
    )
}

SITE_ID = 1

ROOT_URLCONF = 'chatserver.urls'

SECRET_KEY = 'super.secret'

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''


STATIC_ROOT = os.path.join(PROJECT_DIR, 'staticfiles')

# URL that handles the static files served from STATIC_ROOT.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

SESSION_ENGINE = 'redis_sessions_fork.session'

SESSION_REDIS_PREFIX = 'session'

try:
    REDIS_URL = os.environ['REDIS_URL']
    CAPITAL_WS4REDIS_CONNECTION = dj_redis_url.parse(REDIS_URL)
    WS4REDIS_CONNECTION = {
        'host': CAPITAL_WS4REDIS_CONNECTION['HOST'],
        'port': CAPITAL_WS4REDIS_CONNECTION['PORT'],
        'db': CAPITAL_WS4REDIS_CONNECTION['DB'],
        'password': CAPITAL_WS4REDIS_CONNECTION['PASSWORD'],
    }
    SESSION_REDIS_URL=REDIS_URL

except:
    print "REDIS_URL was not found in env"

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'ws4redis.context_processors.default',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.app_directories.Loader',
)

TIME_ZONE = 'Europe/Berlin'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'ws4redis',
    'chatserver',
)

# These two middleware classes must be present, if messages sent or received through a websocket
# connection shall be delivered to an authenticated Django user.
MIDDLEWARE_CLASSES = (
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

# This setting is required to override the Django's main loop, when running in
# development mode, such as ./manage runserver
WSGI_APPLICATION = 'ws4redis.django_runserver.application'

# URL that distinguishes websocket connections from normal requests
WEBSOCKET_URL = '/ws/'

# Set the number of seconds each message shall persited
WS4REDIS_EXPIRE = 3600

WS4REDIS_HEARTBEAT = '--heartbeat--'

WS4REDIS_PREFIX = 'demo'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '[%(asctime)s %(module)s] %(levelname)s: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

ALLOWED_HOSTS = ['*']

