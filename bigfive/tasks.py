from celery import Celery
from celery.schedules import crontab
from celery.decorators import periodic_task
app = Celery()
from celery import task


@app.task
def test(arg):
    print(arg)

@app.task
def whatever(arg):
    print('trying....')
