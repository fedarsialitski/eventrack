from django.urls import path

from venue import views


app_name = 'venue'
urlpatterns = [
    path('venue', views.VenueListView.as_view(), name='venue'),
    path('venue/<int:pk>', views.VenueDetailView.as_view(), name='venue_detail'),
    path('venue/<int:pk>/bookmark', views.bookmark_venue, name='venue_bookmark'),
]
