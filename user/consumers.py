from asgiref.sync import async_to_sync
from channels.generic.websocket import JsonWebsocketConsumer


class UserConsumer(JsonWebsocketConsumer):
    def connect(self):
        user = self.scope['user']
        if user.is_authenticated:
            self.accept()
            group = 'user-{}'.format(user.id)
            async_to_sync(self.channel_layer.group_add)(group, self.channel_name)
        else:
            self.close()

    def disconnect(self, close_code):
        user = self.scope['user']
        group = 'user-{}'.format(user.id)
        async_to_sync(self.channel_layer.group_discard)(group, self.channel_name)

    def event_change(self, event):
        self.send_json(content=event['name'])
