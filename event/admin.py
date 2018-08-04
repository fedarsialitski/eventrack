from django.contrib import admin

from event.models import Event


class EventArtistsInline(admin.TabularInline):
    model = Event.artists.through
    verbose_name_plural = 'Artists'
    extra = 1


class EventInline(admin.StackedInline):
    model = Event
    extra = 1


class EventAdmin(admin.ModelAdmin):
    inlines = [EventArtistsInline]
    list_display = ['title', 'datetime', 'venue']
    list_filter = ['title', 'datetime', 'venue__name']
    search_fields = ['title', 'datetime', 'venue__name']


admin.site.register(Event, EventAdmin)
