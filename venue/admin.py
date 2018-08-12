from django.contrib import admin

from event.admin import EventInline
from venue.models import Venue


class VenueAdmin(admin.ModelAdmin):
    inlines = [EventInline]
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name']


admin.site.register(Venue, VenueAdmin)
