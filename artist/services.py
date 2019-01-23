from songkick.exceptions import SongkickDecodeError, SongkickRequestError

from artist.models import Artist
from eventrack.services import Service


class ArtistService(Service):
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
