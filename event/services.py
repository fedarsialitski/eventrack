from songkick.exceptions import SongkickDecodeError, SongkickRequestError

from artist.services import ArtistService
from event.models import Event
from eventrack.services import Service
from venue.services import VenueService


class EventService(Service):
    def __init__(self):
        self.artist_service = ArtistService()
        self.venue_service = VenueService()
        super().__init__()

    def get_events(self, artist):
        events = set()
        venues = set()
        artists = set()
        locations = set()
        event_artists = dict()

        try:
            artist_events = list(self.songkick.artist_events.query(
                artist_id=artist.pk,
            ))
        except (SongkickDecodeError, SongkickRequestError):
            artist_events = []

        for event in artist_events:
            events.add(self.create_event(event))

            _artists = set()

            for event_artist in event.artists:
                if artist.pk != event_artist.id:
                    _artists.add(self.artist_service.create_artist(event_artist))
            else:
                artists |= _artists
                event_artists[event.id] = _artists

            if event.venue.id:
                venues.add(self.venue_service.create_venue(event))

            if event.venue.metro_area.id:
                locations.add(self.venue_service.create_location(event))

        return events, artists, event_artists, venues, locations

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
