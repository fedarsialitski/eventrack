from django.urls import path

from . import views

app_name = 'event'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('search', views.SearchView.as_view(), name='search'),
    path('artist', views.ArtistListView.as_view(), name='artist'),
    path('artist/add', views.ArtistCreateView.as_view(), name='artist_add'),
    path('artist/<int:pk>/edit', views.ArtistUpdateView.as_view(), name='artist_update'),
    path('artist/<int:pk>/delete', views.ArtistDeleteView.as_view(), name='artist_delete'),
    path('artist/<int:pk>', views.ArtistDetailView.as_view(), name='artist_detail'),
    path('artist/<int:pk>/bookmark', views.bookmark_artist, name='artist_bookmark'),
    path('event', views.EventListView.as_view(), name='event'),
    path('event/add', views.EventCreateView.as_view(), name='event_add'),
    path('event/<int:pk>/edit', views.EventUpdateView.as_view(), name='event_update'),
    path('event/<int:pk>/delete', views.EventDeleteView.as_view(), name='event_delete'),
    path('event/<int:pk>', views.EventDetailView.as_view(), name='event_detail'),
    path('event/<int:pk>/bookmark', views.bookmark_event, name='event_bookmark'),
    path('venue', views.VenueListView.as_view(), name='venue'),
    path('venue/add', views.VenueCreateView.as_view(), name='venue_add'),
    path('venue/<int:pk>/edit', views.VenueUpdateView.as_view(), name='venue_update'),
    path('venue/<int:pk>/delete', views.VenueDeleteView.as_view(), name='venue_delete'),
    path('venue/<int:pk>', views.VenueDetailView.as_view(), name='venue_detail'),
    path('venue/<int:pk>/bookmark', views.bookmark_venue, name='venue_bookmark'),
]
