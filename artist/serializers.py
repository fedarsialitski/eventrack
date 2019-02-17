from rest_framework.serializers import ModelSerializer

from artist.models import Artist


class ArtistSerializer(ModelSerializer):
    class Meta:
        model = Artist
        exclude = ('bandsintown_id', 'mbid', 'events', 'similar_artists')
