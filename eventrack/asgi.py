"""
ASGI config for eventrack project.

It exposes the ASGI callable as a module-level variable named ``channel_layer``.

For more information on this file, see
http://channels.readthedocs.io/en/1.1.8/deploying.html
"""

import os

from channels.asgi import get_channel_layer

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eventrack.settings.prod")

channel_layer = get_channel_layer()
