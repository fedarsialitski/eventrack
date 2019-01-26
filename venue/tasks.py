from django.conf import settings
from django.db import transaction
from django.db.models import Q

from celery import task

from venue.models import Venue
from venue.services import VenueService


@task
def update_venues():
    venues = Venue.objects.select_for_update().filter(
        street='',
    ).exclude(
        ~Q(zip='') |
        ~Q(phone='') |
        ~Q(description='') |
        ~Q(website='') |
        ~Q(capacity__isnull=True)
    )[:settings.VENUES_COUNT]

    venue_service = VenueService()

    with transaction.atomic():
        for venue in venues:
            venue = venue_service.update_venue(venue)
            venue.save()
