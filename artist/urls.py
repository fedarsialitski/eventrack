from django.urls import path

from artist import views


app_name = 'artist'
urlpatterns = [
    path('artist', views.ArtistListView.as_view(), name='artist'),
    path('artist/add', views.ArtistCreateView.as_view(), name='artist_add'),
    path('artist/<int:pk>/edit', views.ArtistUpdateView.as_view(), name='artist_update'),
    path('artist/<int:pk>/delete', views.ArtistDeleteView.as_view(), name='artist_delete'),
    path('artist/<int:pk>', views.ArtistDetailView.as_view(), name='artist_detail'),
    path('artist/<int:pk>/bookmark', views.bookmark_artist, name='artist_bookmark'),
]
