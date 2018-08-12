from django.db import models

from event.models import Event


class Artist(models.Model):
    songkick_id = models.PositiveIntegerField()
    bandsintown_id = models.PositiveIntegerField()

    mbid = models.UUIDField()
    name = models.CharField(max_length=255)

    image_url = models.URLField()
    thumb_url = models.URLField()

    facebook_url = models.URLField()
    songkick_url = models.URLField()
    bandsintown_url = models.URLField()

    events = models.ManyToManyField(
        Event,
        related_name='artists'
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
