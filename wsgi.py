# test uWSGI with low traffic:
# uwsgi --virtualenv $VIRTUAL_ENV --http :9090 --gevent 100 --http-websockets --module wsgi
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatserver.settings')

from django.core.wsgi import get_wsgi_application
from django.conf import settings
from ws4redis.uwsgi_runserver import uWSGIWebsocketServer
from whitenoise.django import DjangoWhiteNoise

application = get_wsgi_application()
_django_app = DjangoWhiteNoise(application)
_websocket_app = uWSGIWebsocketServer()


def application(environ, start_response):
    if environ.get('PATH_INFO').startswith(settings.WEBSOCKET_URL):
        return _websocket_app(environ, start_response)
    return _django_app(environ, start_response)
