from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.URLField(blank=True)
    thumb_url = models.URLField(blank=True)

    events = models.ManyToManyField(
        'event.Event',
        related_name='artists',
        blank=True,
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=200)
    datetime = models.DateTimeField()

    venue = models.ForeignKey(
        'event.Venue',
        related_name='events',
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ['datetime']

    def __str__(self):
        return self.title


class Venue(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    class Meta:
        ordering = [
            'country',
            'city',
            'name',
        ]

    def __str__(self):
        return self.name + ' @ ' + self.city + ', ' + self.country
