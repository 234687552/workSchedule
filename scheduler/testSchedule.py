# -*- coding: utf-8 -*-

import datetime
import time

from scheduler.MyScheduler import Scheduler


def my_job():
    print 'hello world', datetime.datetime.now()


if __name__ == '__main__':
    scheduler = Scheduler.get_instance()
    print time.strftime('%Y-%m-%d ') + time.strftime('%H:%M:%S')
    rundata = time.strftime('%Y-%m-%d ') + time.strftime('%H:%M:') + str((int(time.strftime('%S')) + 5))
    print rundata
    scheduler.addJob(my_job, rundata)
    scheduler.start()
    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()
