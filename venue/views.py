from django.http import JsonResponse
from django.views import generic
from django.contrib.auth.decorators import login_required

from venue.models import Venue


class VenueListView(generic.ListView):
    model = Venue
    paginate_by = 12
    template_name = 'event/pages/venue.html'
    context_object_name = 'venues'


class VenueDetailView(generic.DetailView):
    model = Venue
    template_name = 'event/details/venue_detail.html'


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
