from django.contrib.gis.geos import Point

from eventrack.services import Service
from venue.models import Venue, Location


class VenueService(Service):
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
