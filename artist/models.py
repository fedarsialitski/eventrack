from django.db import models

from event.models import Event


class Artist(models.Model):
    songkick_id = models.IntegerField(primary_key=True)
    bandsintown_id = models.IntegerField(null=True)

    mbid = models.UUIDField(null=True)
    name = models.CharField(max_length=255)

    image_url = models.URLField(default='')
    thumb_url = models.URLField(default='')

    songkick_url = models.URLField(default='')
    bandsintown_url = models.URLField(default='')
    facebook_page_url = models.URLField(default='')

    events = models.ManyToManyField(
        Event,
        related_name='artists'
    )

    similar_artists = models.ManyToManyField(
        'self',
        related_name='similar_artists'
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
