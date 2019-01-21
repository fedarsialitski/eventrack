from django.db import models

from venue.models import Venue


class Event(models.Model):
    songkick_id = models.IntegerField(primary_key=True)
    bandsintown_id = models.IntegerField(null=True)

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255, default='')

    datetime = models.DateTimeField()

    songkick_url = models.URLField(default='')
    bandsintown_url = models.URLField(default='')

    venue = models.ForeignKey(
        Venue,
        related_name='events',
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ['datetime']

    def __str__(self):
        return self.name
