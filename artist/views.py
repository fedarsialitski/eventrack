from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import generic
from django.utils import timezone
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required

from artist.models import Artist
from artist.forms import ArtistForm


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
        context['upcoming_events'].update({'week': events.filter(datetime__gte=now, datetime__week=week).order_by('datetime')})
        context['upcoming_events'].update({'month': events.filter(datetime__gte=now, datetime__month=month).order_by('datetime')})
        context['upcoming_events'].update({'year': events.filter(datetime__gte=now, datetime__year=year).order_by('datetime')})
        context['upcoming_events'].update({'all': events.filter(datetime__gte=now).order_by('datetime')})

        context['past_events'] = {}
        context['past_events'].update({'week': events.filter(datetime__lte=now, datetime__week=week).order_by('-datetime')})
        context['past_events'].update({'month': events.filter(datetime__lte=now, datetime__month=month).order_by('-datetime')})
        context['past_events'].update({'year': events.filter(datetime__lte=now, datetime__year=year).order_by('-datetime')})
        context['past_events'].update({'all': events.filter(datetime__lte=now).order_by('-datetime')})
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
