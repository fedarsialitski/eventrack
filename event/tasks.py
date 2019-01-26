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

    artist_events = dict()
    locations = set()
    venues = set()
    events = set()

    for artist in artists:
        _events, _venues, _locations = event_service.get_events(artist)
        artist_events[artist.pk] = _events
        locations |= _locations
        venues |= _venues
        events |= _events

    location_ids = [location.pk for location in locations]
    venue_ids = [venue.pk for venue in venues]
    event_ids = [event.pk for event in events]

    locations -= set(Location.objects.filter(pk__in=location_ids))
    venues -= set(Venue.objects.filter(pk__in=venue_ids))
    events -= set(Event.objects.filter(pk__in=event_ids))

    Location.objects.bulk_create(locations)
    Venue.objects.bulk_create(venues)

    created_events = set(Event.objects.bulk_create(events))

    for artist in artists:
        unrelated_events = created_events ^ artist_events[artist.pk]
        events_set = created_events - unrelated_events
        if events_set:
            artist.events.set(events_set)
