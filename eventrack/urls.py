from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('', include('event.urls')),
    path('', include('user.urls')),
    path('admin/', admin.site.urls),
]
