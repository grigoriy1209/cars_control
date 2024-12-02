from django.urls import path

from apps.all_cars.listings.consumers import CarConsumer

websocket_urlpatterns = [
    path('', CarConsumer.as_asgi())
]