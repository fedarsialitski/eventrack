from django.db import models


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
