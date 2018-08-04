from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=200)
    datetime = models.DateTimeField()

    venue = models.ForeignKey(
        'venue.Venue',
        related_name='events',
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ['datetime']

    def __str__(self):
        return self.title
