from django.urls import path

from venue import views


app_name = 'venue'
urlpatterns = [
    path('venue', views.VenueListView.as_view(), name='venue'),
    path('venue/add', views.VenueCreateView.as_view(), name='venue_add'),
    path('venue/<int:pk>/edit', views.VenueUpdateView.as_view(), name='venue_update'),
    path('venue/<int:pk>/delete', views.VenueDeleteView.as_view(), name='venue_delete'),
    path('venue/<int:pk>', views.VenueDetailView.as_view(), name='venue_detail'),
    path('venue/<int:pk>/bookmark', views.bookmark_venue, name='venue_bookmark'),
]
