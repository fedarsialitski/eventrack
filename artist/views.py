from django.http import JsonResponse
from django.views import generic
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from rest_framework.viewsets import ReadOnlyModelViewSet

from artist.models import Artist
from artist.serializers import ArtistSerializer


class ArtistViewSet(ReadOnlyModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


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
        context['upcoming_events'].update({'week': events.filter(start__gte=now, start__week=week).order_by('start')})
        context['upcoming_events'].update({'month': events.filter(start__gte=now, start__month=month).order_by('start')})
        context['upcoming_events'].update({'year': events.filter(start__gte=now, start__year=year).order_by('start')})
        context['upcoming_events'].update({'all': events.filter(start__gte=now).order_by('start')})

        context['past_events'] = {}
        context['past_events'].update({'week': events.filter(start__lte=now, start__week=week).order_by('-start')})
        context['past_events'].update({'month': events.filter(start__lte=now, start__month=month).order_by('-start')})
        context['past_events'].update({'year': events.filter(start__lte=now, start__year=year).order_by('-start')})
        context['past_events'].update({'all': events.filter(start__lte=now).order_by('-start')})
        return context


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
