from __future__ import absolute_import
from celery import Celery

app = Celery(
    'celery_main',
    broker='amqp://admin:mypass@rabbit:5672',
    backend='rpc://',
    include=['celery_main.task_receiver']
)
