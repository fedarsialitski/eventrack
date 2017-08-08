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
    context_object_name = 'artists'

    def get_queryset(self):
        """
        Return the first twelve artists
        """
        return Artist.objects.all()[:12]


class ArtistDetailView(generic.DetailView):
    model = Artist

    def get_context_data(self, **kwargs):
        """
        Return the arist detail information
        """
        context = super(ArtistDetailView, self).get_context_data(**kwargs)
        context['upcoming_events'] = self.object.events.filter(
            datetime__gte=timezone.now()
        ).order_by('datetime')
        context['past_events'] = self.object.events.filter(
            datetime__lte=timezone.now()
        ).order_by('-datetime')
        return context


class EventView(generic.ListView):
    model = Event
    template_name = 'event/event.html'
    context_object_name = 'events'

    def get_queryset(self):
        """
        Return the upcoming events
        """
        return Event.objects.filter(
            datetime__gte=timezone.now()
        ).order_by('datetime')[:10]


class EventDetailView(generic.DetailView):
    model = Event

    def get_object(self):
        """
        Return the event detail information
        """
        object = super(EventDetailView, self).get_object()
        return object


class VenueView(generic.ListView):
    model = Venue
    template_name = 'event/venue.html'


class VenueCreateView(generic.CreateView):
    model = Venue
    success_url = '/profile/'

    fields = [
        'name',
        'city',
        'country',
    ]

class VenueUpdateView(generic.UpdateView):
    model = Venue
    success_url = '/profile/'

    fields = [
        'name',
        'city',
        'country',
    ]
