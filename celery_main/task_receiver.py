from __future__ import absolute_import
from celery_main.celery import app
import time
import random


@app.task(bind=True,default_retry_delay=10)
def do_work(self, item):
    print('Task received ' + str(item))
    # sleep for random seconds to simulate a really long task
    time.sleep(random.randint(1, 3))

    result = item + item
    return result



