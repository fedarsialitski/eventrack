import json

from channels import Group
from channels.auth import channel_session_user, channel_session_user_from_http

from django.dispatch import receiver
from django.db.models.signals import post_save

from event.models import Event


@receiver(post_save, sender=Event)
def send_update(sender, instance, **kwargs):
    for user in instance.users.all():
        channel = Group('user-{}'.format(user.id))
        channel.send({
            'text': json.dumps({
                'id': instance.id,
                'title': instance.title,
            })
        })


@channel_session_user_from_http
def ws_connect(message):
    message.reply_channel.send({'accept': True})
    if message.user.is_authenticated:
        Group('user-{}'.format(message.user.id)).add(message.reply_channel)


@channel_session_user
def ws_disconnect(message):
    Group('user-{}'.format(message.user.id)).discard(message.reply_channel)
