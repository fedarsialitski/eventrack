from songkick.exceptions import SongkickDecodeError, SongkickRequestError

from event.models import Event
from eventrack.services import Service
from venue.services import VenueService


class EventService(Service):
    def __init__(self):
        self.venue_service = VenueService()
        super().__init__()

    def get_events(self, artist):
        events = set()
        venues = set()
        locations = set()

        if artist.pk:
            try:
                artist_events = list(self.songkick.artist_events.query(
                    artist_id=artist.pk,
                ))
            except (SongkickDecodeError, SongkickRequestError):
                artist_events = []

            for event in artist_events:
                events.add(self.create_event(event))

                if event.venue.id:
                    venues.add(self.venue_service.create_venue(event))

                if event.venue.metro_area.id:
                    locations.add(self.venue_service.create_location(event))

        return events, venues, locations

    def create_event(self, event):
        end = None

        if event.event_end:
            end = event.event_end.datetime or event.event_end.date

        return Event(
            end=end,
            pk=event.id,
            type=event.event_type,
            name=event.display_name,
            venue_id=event.venue.id,
            location_id=event.venue.metro_area.id,
            songkick_url=self.get_url(event.uri),
            start=event.event_start.datetime or event.event_start.date,
        )
