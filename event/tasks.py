from django.conf import settings

from celery import task

from artist.models import Artist
from event.models import Event
from event.services import EventService
from venue.models import Venue, Location


@task
def fetch_events():
    artists = Artist.objects.all()[:settings.ARTISTS_COUNT]
    event_service = EventService()

    related_artists = dict()
    artist_events = dict()
    event_artists = set()
    locations = set()
    venues = set()
    events = set()

    for artist in artists:
        _events, _artists, _event_artists, _venues, _locations = event_service.get_events(artist)
        related_artists.update(_event_artists)
        artist_events[artist.pk] = _events
        event_artists |= _artists
        locations |= _locations
        venues |= _venues
        events |= _events

    event_artists_ids = [event_artist.pk for event_artist in event_artists]
    location_ids = [location.pk for location in locations]
    venue_ids = [venue.pk for venue in venues]
    event_ids = [event.pk for event in events]

    event_artists -= set(Artist.objects.filter(pk__in=event_artists_ids))
    locations -= set(Location.objects.filter(pk__in=location_ids))
    venues -= set(Venue.objects.filter(pk__in=venue_ids))
    events -= set(Event.objects.filter(pk__in=event_ids))

    Location.objects.bulk_create(locations)
    Venue.objects.bulk_create(venues)

    created_artists = set(Artist.objects.bulk_create(event_artists))
    created_events = set(Event.objects.bulk_create(events))

    for artist in artists:
        unrelated_events = created_events ^ artist_events[artist.pk]
        events_set = created_events - unrelated_events
        if events_set:
            artist.events.set(events_set)

    for event in created_events:
        unrelated_artists = created_artists ^ related_artists[event.pk]
        artists_set = created_artists - unrelated_artists
        if artists_set:
            event.artists.set(artists_set)
