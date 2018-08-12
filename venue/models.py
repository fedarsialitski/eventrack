from django.contrib.gis.db import models


class Location(models.Model):
    songkick_id = models.PositiveIntegerField()

    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    coordinates = models.PointField()

    songkick_url = models.URLField()

    class Meta:
        ordering = ['country', 'city']

    def __str__(self):
        return '{}, {}'.format(self.city, self.country)


class Venue(models.Model):
    songkick_id = models.PositiveIntegerField()

    zip = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    street = models.CharField(max_length=255)

    capacity = models.PositiveIntegerField()
    description = models.TextField()

    coordinates = models.PointField()

    website = models.URLField()
    songkick_url = models.URLField()

    location = models.ForeignKey(
        Location,
        related_name='venues',
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return '{} @ {}'.format(self.name, self.location)
