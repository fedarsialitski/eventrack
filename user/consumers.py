import json

from channels import Group
from channels.auth import channel_session_user, channel_session_user_from_http

from django.dispatch import receiver
from django.db.models.signals import post_save

from event.models import Event


@receiver(post_save, sender=Event)
def send_update(sender, instance, **kwargs):
    Group('users').send({
        'text': json.dumps({
            'id': instance.id,
            'title': instance.title,
        })
    })


@channel_session_user_from_http
def ws_connect(message):
    Group('users').add(message.reply_channel)
    message.reply_channel.send({
        'accept': True
    })


@channel_session_user
def ws_disconnect(message):
    Group('users').discard(message.reply_channel)
