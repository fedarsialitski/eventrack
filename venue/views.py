from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin

from venue.forms import VenueForm
from venue.models import Venue


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
