from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from event.models import Event


class EventSerializer(ModelSerializer):
    thumb_url = SerializerMethodField()

    class Meta:
        model = Event
        exclude = ('venue', 'location')

    @staticmethod
    def get_thumb_url(instance):
        return instance.artists.first().thumb_url
