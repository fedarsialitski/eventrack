from django.contrib import admin

from artist.models import Artist


class ArtistEventsInline(admin.TabularInline):
    model = Artist.events.through
    verbose_name_plural = 'Events'
    extra = 1


class ArtistAdmin(admin.ModelAdmin):
    inlines = [ArtistEventsInline]
    exclude = ('events',)
    search_fields = ['name']


admin.site.register(Artist, ArtistAdmin)
