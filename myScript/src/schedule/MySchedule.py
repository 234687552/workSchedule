# -*- coding: utf-8 -*-
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
def my_job():
    print 'hello world',datetime.datetime.now()

sched = BlockingScheduler()
sched.add_job(my_job, 'interval', seconds=5)

sched.start()
