from django.shortcuts import render
from django.views import generic
from django.utils import timezone

from .models import Artist, Event, Venue


class IndexView(generic.ListView):
    template_name = 'event/index.html'
    context_object_name = 'upcoming_events_list'

    def get_queryset(self):
        """
        Return the five upcoming events
        """
        return Event.objects.filter(
            datetime__gte=timezone.now()
        ).order_by('-datetime')[:5]


class ArtistView(generic.ListView):
    model = Artist
    template_name = 'event/artist.html'


class EventView(generic.ListView):
    model = Event
    template_name = 'event/event.html'


class VenueView(generic.ListView):
    model = Venue
    template_name = 'event/venue.html'


class ProfileView(generic.ListView):
    pass
