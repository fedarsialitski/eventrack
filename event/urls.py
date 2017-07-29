from django.conf.urls import url

from . import views

app_name = 'event'
urlpatterns = [
    url(r'^home/$', views.IndexView.as_view(), name='index'),
    url(r'^artist/$', views.ArtistView.as_view(), name='artist'),
    url(r'^artist/(?P<pk>\d+)/$', views.ArtistDetailView.as_view(), name='artist_detail'),
    url(r'^event/$', views.EventView.as_view(), name='event'),
    url(r'^venue/$', views.VenueView.as_view(), name='venue'),
    url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
]
