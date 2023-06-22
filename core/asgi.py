import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

from chat import routing as chat_routing
from timer import routing as timer_routing
from graph import routing as graph_routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
django_asgi_app = get_asgi_application()

urls = []
urls += chat_routing.websocket_urlpatterns 
urls += timer_routing.ws_urlpatterns 
urls += graph_routing.ws_urlpatterns 

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(urls)
        ))
    }
)

# application = get_asgi_application()
