from songkick.exceptions import SongkickDecodeError, SongkickRequestError

from artist.models import Artist
from eventrack.services import Service


class ArtistService(Service):
    def get_artist_data(self, artist):
        return self.bandsintown.artists(artist.name) or {}

    def get_similar_artists(self, artist):
        artists = set()

        if artist.pk:
            try:
                similar_artists = list(self.songkick.artists_similar.query(
                    artist_id=artist.pk,
                ))
            except (SongkickDecodeError, SongkickRequestError):
                similar_artists = []

            for similar_artist in similar_artists:
                artists.add(self.create_artist(similar_artist))

        return artists

    def create_artist(self, artist):
        return Artist(
            pk=artist.id,
            name=artist.display_name,
            songkick_url=self.get_url(artist.songkick_uri),
        )

    def update_artist(self, artist):
        data = self.get_artist_data(artist)

        data['bandsintown_id'] = data.pop('id', None)
        data['bandsintown_url'] = self.get_url(data.pop('url', None))

        for key, value in data.items():
            if value:
                setattr(artist, key, value)

        return artist
