# entry point for the websocket loop
import gevent.socket
import redis.connection
redis.connection.socket = gevent.socket
from ws4redis.uwsgi_runserver import uWSGIWebsocketServer
application = uWSGIWebsocketServer()
