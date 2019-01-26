from asgiref.sync import async_to_sync
from django.db.models.signals import post_save

from event.models import Event
from channels.layers import get_channel_layer


def post_save_event_signal_handler(instance, **kwargs):
    channel_layer = get_channel_layer()
    for user in instance.users.all():
        group = "user-{}".format(user.id)
        message = {
            'type': 'event.change',
            'text': {
                'id': instance.id,
                'name': instance.name,
                'date': instance.start.strftime('%Y/%m/%d'),
            }
        }
        async_to_sync(channel_layer.group_send)(group, message)


def register_signal_handlers():
    post_save.connect(post_save_event_signal_handler, sender=Event)
