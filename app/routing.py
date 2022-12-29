from django.urls import path
from app.consumers import EchoConsumer

websocket_patterns = [
    path('ws/echo/', EchoConsumer.as_asgi()),
]