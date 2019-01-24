from django.conf import settings
from django.db import transaction

from celery import task

from artist.models import Artist
from artist.services import ArtistService


@task
def fetch_similar_artists():
    artists = Artist.objects.all()[:settings.ARTISTS_COUNT]
    artist_service = ArtistService()

    similar_artists = set()
    related_artists = dict()

    for artist in artists:
        fetched_artists = artist_service.get_similar_artists(artist)
        similar_artists |= fetched_artists
        related_artists[artist.songkick_id] = fetched_artists

    ids = [similar_artist.songkick_id for similar_artist in similar_artists]

    similar_artists -= set(Artist.objects.filter(songkick_id__in=ids))
    created_artists = set(Artist.objects.bulk_create(similar_artists))

    for artist in artists:
        unrelated_artists = created_artists ^ related_artists[artist.songkick_id]
        artist.similar_artists.set(created_artists - unrelated_artists)


@task
def update_artists():
    artists = Artist.objects.select_for_update().filter(
        bandsintown_id__isnull=True,
    )[:settings.ARTISTS_COUNT]

    artist_service = ArtistService()

    with transaction.atomic():
        for artist in artists:
            artist = artist_service.update_artist(artist)
            artist.save()
