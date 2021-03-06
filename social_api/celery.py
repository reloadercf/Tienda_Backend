from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings


#seteamos el default
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'social_api.settings')

app = Celery('social_api', 
			broker="amqp://eric:ericdelaparra@localhost/eric_vhost")

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

