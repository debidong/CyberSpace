from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.urls import path


# application = ProtocolTypeRouter(
#     {
#         'http': get_asgi_application(),
#         'websocket': URLRouter([
#             path('ws/my-path/', MyConsumer.as_asgi()),
#         ]),
#     }
# )
