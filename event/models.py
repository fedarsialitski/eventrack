from django.db import models

from venue.models import Venue, Location


class Event(models.Model):
    songkick_id = models.IntegerField(primary_key=True)

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255, default='')

    start = models.DateTimeField()
    end = models.DateTimeField(null=True)

    songkick_url = models.URLField(default='')

    venue = models.ForeignKey(
        Venue,
        null=True,
        related_name='events',
        on_delete=models.CASCADE,
    )

    location = models.ForeignKey(
        Location,
        null=True,
        related_name='events',
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ['start']

    def __str__(self):
        return self.name
