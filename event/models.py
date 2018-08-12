from django.db import models

from venue.models import Venue


class Event(models.Model):
    songkick_id = models.PositiveIntegerField()
    bandsintown_id = models.PositiveIntegerField()

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)

    datetime = models.DateTimeField()
    description = models.TextField()

    songkick_url = models.URLField()
    bandsintown_url = models.URLField()

    venue = models.ForeignKey(
        Venue,
        related_name='events',
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ['datetime']

    def __str__(self):
        return self.name
