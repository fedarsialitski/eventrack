from django.apps import AppConfig


class UserConfig(AppConfig):
    name = 'user'

    def ready(self):
        from user.signal_handlers import register_signal_handlers
        register_signal_handlers()
