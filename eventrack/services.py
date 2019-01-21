from django.conf import settings

from bandsintown import Client as Bandsintown
from songkick import Songkick


class Service:
    def __init__(self):
        self.bandsintown = Bandsintown(settings.BANDSINTOWN_APP_ID)
        self.songkick = Songkick(settings.SONGKICK_API_KEY)
