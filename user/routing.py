from django.conf.urls import url

from user.consumers import UserConsumer


websocket_urlpatterns = [
    url(r'^ws$', UserConsumer),
]
