# entry point for the websocket loop
import os
import gevent.socket
import redis.connection
redis.connection.socket = gevent.socket
if not os.environ.has_key('DJANGO_SETTINGS_MODULE'):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatserver.settings')
from ws4redis.uwsgi_runserver import uWSGIWebsocketServer
application = uWSGIWebsocketServer()