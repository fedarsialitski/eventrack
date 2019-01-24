from songkick.exceptions import SongkickDecodeError, SongkickRequestError

from artist.models import Artist
from eventrack.services import Service


class ArtistService(Service):
    def get_artist_data(self, artist):
        return self.bandsintown.artists(artist.name) or {}

    def get_similar_artists(self, artist):
        artists = set()

        if artist.songkick_id:
            try:
                similar_artists = self.songkick.artists_similar.query(
                    artist_id=artist.songkick_id,
                )
            except (SongkickDecodeError, SongkickRequestError):
                similar_artists = []

            for similar_artist in similar_artists:
                artists.add(Artist(
                    name=similar_artist.display_name,
                    songkick_id=similar_artist.id,
                    songkick_url=self.get_url(similar_artist.songkick_uri),
                ))

        return artists

    def update_artist(self, artist):
        data = self.get_artist_data(artist)

        data['bandsintown_id'] = data.pop('id', None)
        data['bandsintown_url'] = self.get_url(data.pop('url', None))

        for key, value in data.items():
            if value:
                setattr(artist, key, value)

        return artist
