from django.conf.urls import url

from . import views

app_name = 'event'
urlpatterns = [
    url(r'^home/$',                      views.IndexView.as_view(),        name='index'),
    url(r'^artist/$',                    views.ArtistView.as_view(),       name='artist'),
    url(r'^artist/(?P<pk>\d+)/$',        views.ArtistDetailView.as_view(), name='artist_detail'),
    url(r'^artist/add/$',                views.ArtistCreateView.as_view(), name='artist_add'),
    url(r'^artist/(?P<pk>\d+)/edit/$',   views.ArtistUpdateView.as_view(), name='artist_update'),
    url(r'^artist/(?P<pk>\d+)/delete/$', views.ArtistDeleteView.as_view(), name='artist_delete'),
    url(r'^event/$',                     views.EventView.as_view(),        name='event'),
    url(r'^event/(?P<pk>\d+)/$',         views.EventDetailView.as_view(),  name='event_detail'),
    url(r'^event/add/$',                 views.EventCreateView.as_view(),  name='event_add'),
    url(r'^event/(?P<pk>\d+)/edit/$',    views.EventUpdateView.as_view(),  name='event_update'),
    url(r'^event/(?P<pk>\d+)/delete/$',  views.EventDeleteView.as_view(),  name='event_delete'),
    url(r'^venue/$',                     views.VenueView.as_view(),        name='venue'),
    url(r'^venue/add/$',                 views.VenueCreateView.as_view(),  name='venue_add'),
    url(r'^venue/(?P<pk>\d+)/edit/$',    views.VenueUpdateView.as_view(),  name='venue_update'),
    url(r'^venue/(?P<pk>\d+)/delete/$',  views.VenueDeleteView.as_view(),  name='venue_delete'),
]
