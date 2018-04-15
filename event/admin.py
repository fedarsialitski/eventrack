from django.contrib import admin
from .models import Artist, Event, Venue


class ArtistEventsInline(admin.TabularInline):
    model = Artist.events.through
    verbose_name_plural = 'Events'
    extra = 1


class EventArtistsInline(admin.TabularInline):
    model = Event.artists.through
    verbose_name_plural = 'Artists'
    extra = 1


class EventInline(admin.StackedInline):
    model = Event
    extra = 1


class ArtistAdmin(admin.ModelAdmin):
    inlines = [ArtistEventsInline]
    exclude = ('events',)
    search_fields = ['name']


class EventAdmin(admin.ModelAdmin):
    inlines = [EventArtistsInline]
    list_display = ['title', 'datetime', 'venue']
    list_filter = ['title', 'datetime', 'venue__name']
    search_fields = ['title', 'datetime', 'venue__name']


class VenueAdmin(admin.ModelAdmin):
    inlines = [EventInline]
    list_display = ['name', 'city', 'country']
    list_filter = ['name', 'city', 'country']
    search_fields = ['name', 'city', 'country']


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Venue, VenueAdmin)
