# -*- coding: utf-8 -*-
from apscheduler.schedulers.background import BackgroundScheduler


# instance1 = Singleton.get_instance() 单利模式  使用:from scheduler.MyScheduler import Scheduler
class Scheduler(object):
    # 定义静态变量实例
    __singleton = None

    def __init__(self):
        self.scheduler = BackgroundScheduler()
        self.scheduler.start()
        pass

    @staticmethod
    def getInstance():
        if Scheduler.__singleton is None:
            Scheduler.__singleton = Scheduler()
        return Scheduler.__singleton

    def getScheduler(self):
        return self.scheduler

        # def addJob(self, job,rundata):
        #     # scheduler.add_job(my_job, 'interval', seconds=3)
        #     # scheduler.add_job(my_job, 'cron', day_of_week='6', second='*/5')
        #     # scheduler.add_job(my_job, 'date', run_date='2016-02-14 15:01:05')
        #
        #     self.scheduler.add_job(job, 'date', run_date=rundata)
        #
        #     '''
        #         year (int|str) – 4-digit year
        #         month (int|str) – month (1-12)
        #         day (int|str) – day of the (1-31)
        #         week (int|str) – ISO week (1-53)
        #         day_of_week (int|str) – number or name of weekday (0-6 or mon,tue,wed,thu,fri,sat,sun)
        #         hour (int|str) – hour (0-23)
        #         minute (int|str) – minute (0-59)
        #         second (int|str) – second (0-59)
        #
        #         start_date (datetime|str) – earliest possible date/time to trigger on (inclusive)
        #         end_date (datetime|str) – latest possible date/time to trigger on (inclusive)
        #         timezone (datetime.tzinfo|str) – time zone to use for the date/time calculations (defaults to scheduler timezone)
        #
        #         *    any    Fire on every value
        #         */a    any    Fire every a values, starting from the minimum
        #         a-b    any    Fire on any value within the a-b range (a must be smaller than b)
        #         a-b/c    any    Fire every c values within the a-b range
        #         xth y    day    Fire on the x -th occurrence of weekday y within the month
        #         last x    day    Fire on the last occurrence of weekday x within the month
        #         last    day    Fire on the last day within the month
        #         x,y,z    any    Fire on any matching expression; can combine any number of any of the above expressions
        #     '''
