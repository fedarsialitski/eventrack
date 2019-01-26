from django.contrib.gis.geos import Point

from songkick.exceptions import SongkickDecodeError, SongkickRequestError

from eventrack.services import Service
from venue.models import Venue, Location


class VenueService(Service):
    def get_venue_data(self, venue):
        try:
            data = next(self.songkick.venue_details.query(venue_id=venue.pk))
        except (SongkickDecodeError, SongkickRequestError, StopIteration):
            data = None

        return data

    def update_venue(self, venue):
        data = self.get_venue_data(venue)

        if data:
            venue = self.update(venue, getattr(data, '_data', {}))

        return venue

    def create_venue(self, event):
        return Venue(
            pk=event.venue.id,
            name=event.venue.display_name,
            location_id=event.venue.metro_area.id,
            coordinates=Point(event.venue.longitude, event.venue.latitude),
            songkick_url=self.get_url(event.venue.uri),
        )

    @staticmethod
    def create_location(event):
        return Location(
            pk=event.venue.metro_area.id,
            city=event.venue.metro_area.display_name,
            state=event.venue.metro_area.state or '',
            country=event.venue.metro_area.country,
            coordinates=Point(event.location.longitude, event.location.latitude),
        )
