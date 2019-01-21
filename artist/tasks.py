from django.conf import settings

from celery import task

from artist.models import Artist
from artist.services import ArtistService


@task
def fetch_similar_artists():
    artists = Artist.objects.all()[:settings.ARTISTS_COUNT]
    artist_service = ArtistService()

    similar_artists = set()

    for artist in artists:
        similar_artists.update(artist_service.get_similar_artists(artist))

    ids = [similar_artist.songkick_id for similar_artist in similar_artists]

    similar_artists.difference_update(Artist.objects.filter(songkick_id__in=ids))

    Artist.objects.bulk_create(similar_artists)
