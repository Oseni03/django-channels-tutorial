from django.urls import path 

from .consumers import TimerConsumer

ws_urlpatterns = [
    path("ws/timer/", TimerConsumer.as_asgi()),
]