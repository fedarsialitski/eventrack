import json

from channels import Group

from django.db.models.signals import post_save

from event.models import Event


def post_save_event_signal_handler(instance, **kwargs):
    for user in instance.users.all():
        channel = Group('user-{}'.format(user.id))
        channel.send({
            'text': json.dumps({
                'id': instance.id,
                'title': instance.title,
                'date': instance.datetime.strftime('%Y/%m/%d'),
            })
        })


def register_signal_handlers():
    post_save.connect(post_save_event_signal_handler, sender=Event)
