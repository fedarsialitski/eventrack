from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    artists = models.ManyToManyField(
        'event.Artist',
        related_name='users',
        blank=True,
    )

    events = models.ManyToManyField(
        'event.Event',
        related_name='users',
        blank=True,
    )
