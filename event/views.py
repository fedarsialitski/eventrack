from django.http import JsonResponse
from django.views import generic
from django.utils import timezone
from django.db.models import Count, Q
from django.contrib.auth.decorators import login_required

from artist.models import Artist
from event.models import Event
from event.forms import SearchForm


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
        if self.request.user.is_authenticated:
            user_artists = self.request.user.artists.all()

            # Exclude artists already followed by a current user
            context['discover'] = context['discover'].exclude(pk__in=user_artists)

            # Get upcoming events by a user's favorite artists
            context['recommend'] = events.filter(artists__in=user_artists, start__gte=now)
            # Exclude events already followed by a current user
            context['recommend'] = context['recommend'].exclude(users__in=[user_id]).annotate(user_count=user_count)
            context['recommend'] = context['recommend'].order_by('start', '-user_count')[:recommend_count]

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
                Q(name__search=keyword) |
                Q(venue__name__search=keyword) |
                Q(venue__location__city__search=keyword) |
                Q(venue__location__country__search=keyword) |
                Q(artists__name__search=keyword)
            ).distinct()
        return Event.objects.all()


class EventListView(generic.ListView):
    model = Event
    paginate_by = 12
    template_name = 'event/pages/event.html'
    context_object_name = 'events'

    def get_queryset(self):
        """
        Return the upcoming events
        """
        return super().get_queryset().filter(start__gte=timezone.now())


class EventDetailView(generic.DetailView):
    model = Event
    template_name = 'event/details/event_detail.html'


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
