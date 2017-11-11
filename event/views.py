from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import generic
from django.utils import timezone
from django.db.models import Count, Q
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import Artist, Event, Venue
from .forms import ArtistForm, EventForm, VenueForm, SearchForm


class IndexView(generic.ListView):
    model = Artist
    template_name = 'event/pages/index.html'
    discover_count = 5
    trending_count = 8
    recommend_count = 10

    def get_context_data(self, **kwargs):
        """
        Return the discover, trending,
        recommended artists and events
        """
        now = timezone.now()
        events = Event.objects
        artists = Artist.objects
        user_id = self.request.user.id
        user_count = Count('users')
        discover_count = self.discover_count
        trending_count = self.trending_count
        recommend_count = self.recommend_count

        context = super(IndexView, self).get_context_data(**kwargs)

        # Get all artists, but exclude artists without images
        context['discover'] = artists.exclude(image_url__exact='', thumb_url__exact='')
        # Get trending artists
        context['trending'] = artists.annotate(user_count=user_count).order_by('-user_count')[:trending_count]
        if self.request.user.is_authenticated():
            user_artists = self.request.user.artists.all()

            # Exclude artists already followed by a current user
            context['discover'] = context['discover'].exclude(pk__in=user_artists)

            # Get upcoming events by a user's favorite artists
            context['recommend'] = events.filter(artists__in=user_artists, datetime__gte=now)
            # Exclude events already followed by a current user
            context['recommend'] = context['recommend'].exclude(users__in=[user_id]).annotate(user_count=user_count)
            context['recommend'] = context['recommend'].order_by('datetime', '-user_count')[:recommend_count]

        context['discover'] = context['discover'][:discover_count]
        return context


class SearchView(generic.ListView):
    model = Event
    form_class = SearchForm
    paginate_by = 12
    template_name = 'event/pages/search.html'
    context_object_name = 'events'

    def get_queryset(self):
        """
        Return the events found by keyword
        """
        form = self.form_class(self.request.GET)
        if form.is_valid():
            keyword = form.cleaned_data['keyword']
            return Event.objects.filter(
                Q(title__search=keyword) |
                Q(venue__name__search=keyword) |
                Q(venue__city__search=keyword) |
                Q(venue__country__search=keyword) |
                Q(artists__name__search=keyword)
            ).distinct()
        return Event.objects.all()


class ArtistListView(generic.ListView):
    model = Artist
    paginate_by = 12
    template_name = 'event/pages/artist.html'
    context_object_name = 'artists'


class ArtistDetailView(generic.DetailView):
    model = Artist
    template_name = 'event/details/artist_detail.html'

    def get_context_data(self, **kwargs):
        """
        Return the artist detail information
        """
        now = timezone.now()
        today = now.date()
        year = today.year
        week = today.isocalendar()[1]
        month = today.month
        events = self.object.events

        context = super(ArtistDetailView, self).get_context_data(**kwargs)

        context['upcoming_events'] = {}
        context['upcoming_events'].update({'week':  events.filter(datetime__gte=now, datetime__week=week).order_by('datetime')})
        context['upcoming_events'].update({'month': events.filter(datetime__gte=now, datetime__month=month).order_by('datetime')})
        context['upcoming_events'].update({'year':  events.filter(datetime__gte=now, datetime__year=year).order_by('datetime')})
        context['upcoming_events'].update({'all':   events.filter(datetime__gte=now).order_by('datetime')})

        context['past_events'] = {}
        context['past_events'].update({'week':  events.filter(datetime__lte=now, datetime__week=week).order_by('-datetime')})
        context['past_events'].update({'month': events.filter(datetime__lte=now, datetime__month=month).order_by('-datetime')})
        context['past_events'].update({'year':  events.filter(datetime__lte=now, datetime__year=year).order_by('-datetime')})
        context['past_events'].update({'all':   events.filter(datetime__lte=now).order_by('-datetime')})
        return context


class ArtistCreateView(PermissionRequiredMixin, generic.CreateView):
    model = Artist
    form_class = ArtistForm
    success_url = reverse_lazy('user:profile')
    template_name = 'event/forms/artist_form.html'
    raise_exception = True
    permission_required = 'event.add_artist'

    def form_valid(self, form):
        """
        Create the artist
        """
        self.request.user.artists.add(form.save())
        return super(ArtistCreateView, self).form_valid(form)


class ArtistUpdateView(PermissionRequiredMixin, generic.UpdateView):
    model = Artist
    form_class = ArtistForm
    success_url = reverse_lazy('user:profile')
    template_name = 'event/forms/artist_form.html'
    raise_exception = True
    permission_required = 'event.change_artist'


class ArtistDeleteView(PermissionRequiredMixin, generic.DeleteView):
    model = Artist
    success_url = reverse_lazy('user:profile')
    raise_exception = True
    permission_required = 'event.delete_artist'


class EventListView(generic.ListView):
    model = Event
    paginate_by = 12
    template_name = 'event/pages/event.html'
    context_object_name = 'events'

    def get_queryset(self):
        """
        Return the upcoming events
        """
        return super().get_queryset().filter(datetime__gte=timezone.now())


class EventDetailView(generic.DetailView):
    model = Event
    template_name = 'event/details/event_detail.html'


class EventCreateView(PermissionRequiredMixin, generic.CreateView):
    model = Event
    form_class = EventForm
    success_url = reverse_lazy('user:profile')
    template_name = 'event/forms/event_form.html'
    raise_exception = True
    permission_required = 'event.add_event'

    def form_valid(self, form):
        """
        Create the event
        """
        self.request.user.events.add(form.save())
        form.instance.artists.set(form.cleaned_data['artists'])
        return super(EventCreateView, self).form_valid(form)


class EventUpdateView(PermissionRequiredMixin, generic.UpdateView):
    model = Event
    form_class = EventForm
    success_url = reverse_lazy('user:profile')
    template_name = 'event/forms/event_form.html'
    raise_exception = True
    permission_required = 'event.change_event'

    def form_valid(self, form):
        """
        Update the event
        """
        form.instance.artists.set(form.cleaned_data['artists'])
        return super(EventUpdateView, self).form_valid(form)


class EventDeleteView(PermissionRequiredMixin, generic.DeleteView):
    model = Event
    success_url = reverse_lazy('user:profile')
    raise_exception = True
    permission_required = 'event.delete_event'


class VenueListView(generic.ListView):
    model = Venue
    paginate_by = 12
    template_name = 'event/pages/venue.html'
    context_object_name = 'venues'


class VenueDetailView(generic.DetailView):
    model = Venue
    template_name = 'event/details/venue_detail.html'


class VenueCreateView(PermissionRequiredMixin, generic.CreateView):
    model = Venue
    form_class = VenueForm
    success_url = reverse_lazy('user:profile')
    template_name = 'event/forms/venue_form.html'
    raise_exception = True
    permission_required = 'event.add_venue'

    def form_valid(self, form):
        """
        Create the venue
        """
        self.request.user.venues.add(form.save())
        return super(VenueCreateView, self).form_valid(form)


class VenueUpdateView(PermissionRequiredMixin, generic.UpdateView):
    model = Venue
    form_class = VenueForm
    success_url = reverse_lazy('user:profile')
    template_name = 'event/forms/venue_form.html'
    raise_exception = True
    permission_required = 'event.change_venue'


class VenueDeleteView(PermissionRequiredMixin, generic.DeleteView):
    model = Venue
    success_url = reverse_lazy('user:profile')
    raise_exception = True
    permission_required = 'event.delete_venue'


@login_required(redirect_field_name='redirect')
def bookmark_artist(request, pk):
    if request.user.artists.filter(id=pk):
        request.user.artists.remove(pk)
    else:
        request.user.artists.add(pk)

    return JsonResponse({
        'pk': pk,
        'id': 'artists',
        'user_count': Artist.objects.get(pk=pk).users.count(),
        'artist_count': request.user.artists.count(),
    })


@login_required(redirect_field_name='redirect')
def bookmark_event(request, pk):
    if request.user.events.filter(id=pk):
        request.user.events.remove(pk)
    else:
        request.user.events.add(pk)

    return JsonResponse({
        'pk': pk,
        'id': 'events',
        'user_count': Event.objects.get(pk=pk).users.count(),
        'event_count': request.user.events.count(),
    })


@login_required(redirect_field_name='redirect')
def bookmark_venue(request, pk):
    if request.user.venues.filter(id=pk):
        request.user.venues.remove(pk)
    else:
        request.user.venues.add(pk)

    return JsonResponse({
        'pk': pk,
        'id': 'venues',
        'user_count': Venue.objects.get(pk=pk).users.count(),
        'venue_count': request.user.venues.count(),
    })
