from django.contrib import admin

from event.admin import EventInline
from venue.models import Venue


class VenueAdmin(admin.ModelAdmin):
    inlines = [EventInline]
    list_display = ['name', 'city', 'country']
    list_filter = ['name', 'city', 'country']
    search_fields = ['name', 'city', 'country']


admin.site.register(Venue, VenueAdmin)
