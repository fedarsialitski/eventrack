from django.urls import include, path
from django.contrib import admin

from rest_framework.routers import SimpleRouter

from artist.views import ArtistViewSet
from event.views import EventViewSet

router = SimpleRouter(trailing_slash=False)

router.register(r'artists', ArtistViewSet)
router.register(r'events', EventViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', include('artist.urls')),
    path('', include('event.urls')),
    path('', include('venue.urls')),
    path('', include('user.urls')),
    path('admin/', admin.site.urls),
]
