from django.views import generic
from django.utils import timezone

from .models import Artist, Event, Venue
from .forms import ArtistForm, EventForm, VenueForm


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
        Return the artist detail information
        """
        context = super(ArtistDetailView, self).get_context_data(**kwargs)
        context['upcoming_events'] = self.object.events.filter(
            datetime__gte=timezone.now()
        ).order_by('datetime')
        context['past_events'] = self.object.events.filter(
            datetime__lte=timezone.now()
        ).order_by('-datetime')
        return context


class ArtistCreateView(generic.CreateView):
    model = Artist
    form_class = ArtistForm
    success_url = '/profile/'

    def form_valid(self, form):
        """
        Create the artist
        """
        self.request.user.artists.add(form.save())
        return super(ArtistCreateView, self).form_valid(form)


class ArtistUpdateView(generic.UpdateView):
    model = Artist
    form_class = ArtistForm
    success_url = '/profile/'


class ArtistDeleteView(generic.DeleteView):
    model = Artist
    success_url = '/profile/'

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)


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

    def get_object(self, queryset=None):
        """
        Return the event detail information
        """
        return super(EventDetailView, self).get_object()


class EventCreateView(generic.CreateView):
    model = Event
    form_class = EventForm
    success_url = '/profile/'

    def form_valid(self, form):
        """
        Create the event
        """
        self.request.user.events.add(form.save())
        form.instance.artists.set(form.cleaned_data['artists'])
        return super(EventCreateView, self).form_valid(form)


class EventUpdateView(generic.UpdateView):
    model = Event
    form_class = EventForm
    success_url = '/profile/'

    def form_valid(self, form):
        """
        Update the event
        """
        form.instance.artists.set(form.cleaned_data['artists'])
        return super(EventUpdateView, self).form_valid(form)


class EventDeleteView(generic.DeleteView):
    model = Event
    success_url = '/profile/'

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)


class VenueView(generic.ListView):
    model = Venue
    template_name = 'event/venue.html'


class VenueCreateView(generic.CreateView):
    model = Venue
    form_class = VenueForm
    success_url = '/profile/'

    def form_valid(self, form):
        """
        Create the venue
        """
        self.request.user.venues.add(form.save())
        return super(VenueCreateView, self).form_valid(form)


class VenueUpdateView(generic.UpdateView):
    model = Venue
    form_class = VenueForm
    success_url = '/profile/'


class VenueDeleteView(generic.DeleteView):
    model = Venue
    success_url = '/profile/'

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)
