from django.urls import path

from artist import views


app_name = 'artist'
urlpatterns = [
    path('artist', views.ArtistListView.as_view(), name='artist'),
    path('artist/<int:pk>', views.ArtistDetailView.as_view(), name='artist_detail'),
    path('artist/<int:pk>/bookmark', views.bookmark_artist, name='artist_bookmark'),
]
