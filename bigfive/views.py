from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
# from .tasks import count_beans, try_thrice
import datetime

import random
# set the default Django settings module for the 'celery' program.

from datetime import timedelta
from . import tasks


from django_celery_beat.models import PeriodicTask, IntervalSchedule


class auction(Page):
    def vars_for_template(self):
        schedule, created = IntervalSchedule.objects.get_or_create(
             every=10,
             period=IntervalSchedule.SECONDS,
           )
        schedule.save()
        a = PeriodicTask.objects.get_or_create(
            interval=schedule,
            name='printing something',
            task='tasks.whatever',
            )


class Results(Page):
    ...


page_sequence = [
    auction,
    Results,
]
