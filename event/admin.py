from django.contrib import admin
from .models import Artist, Event, Venue


admin.site.register(Artist)
admin.site.register(Event)
admin.site.register(Venue)
