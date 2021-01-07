from gevent import monkey
monkey.patch_all() 


import os
from celery import Celery
from celery.schedules import crontab
from datetime import datetime
from worker1.workflows.workflow1 import get_time
from worker1.workflows.workflow2 import print_time

REDIS = f'redis://:{os.environ.get("REDIS_PASSWORD")}@redis:6379/0'

app = Celery('main', broker=REDIS, backend=REDIS)
app.conf.beat_schedule = {
    "every-ten-seconds-task": {
        "task": "worker1.main.proxy_get_time",
        "schedule": 10.0,
        "args": (str(datetime.now()),),
    },

    "every-minute-task": {
        "task": "worker1.main.proxy_print_time",
        "schedule": crontab(), # per minute
    }
}


@app.task
def proxy_get_time(timestamp):
    return get_time(timestamp)  # The task results can be retrieved from Redis using the timestamp as args


@app.task
def proxy_print_time():
    return print_time() 

