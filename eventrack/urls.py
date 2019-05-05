from django.urls import include, path
from django.contrib import admin
from django.contrib.staticfiles.templatetags.staticfiles import static

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework import permissions
from rest_framework.routers import SimpleRouter

from artist.views import ArtistViewSet
from event.views import EventViewSet

router = SimpleRouter(trailing_slash=False)

router.register(r'artists', ArtistViewSet)
router.register(r'events', EventViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title='Eventrack API',
        default_version='v1.0',
        x_logo={
            "url": static("event/images/logo.png"),
            "backgroundColor": "#FAFAFA"
        }
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', include('artist.urls')),
    path('', include('event.urls')),
    path('', include('venue.urls')),
    path('', include('user.urls')),
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='docs'),
]
