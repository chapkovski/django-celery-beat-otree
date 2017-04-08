from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from celery.decorators import periodic_task
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
from datetime import timedelta
from . import tasks
app = Celery('bigfive', broker='redis://localhost:6379/5')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
