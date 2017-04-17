# -*- coding: cp936 -*-
'''
软件所有事件控制
'''
import datetime

from src.scheduler.Scheduler import Scheduler
from apscheduler.triggers.interval import IntervalTrigger
from src.wxpython.MyDialog import MyDialog



class EventCtrl(object):
    # 定义静态变量实例
    __singleton = None

    def __init__(self):
        self.start = False  # 默认是没开始
        self.scheduler = Scheduler.getInstance().getScheduler()
        pass

    @staticmethod
    def getInstance():
        if EventCtrl.__singleton is None:
            EventCtrl.__singleton = EventCtrl()
        return EventCtrl.__singleton

    def onStartToggle(self, Frame):
        if self.start:
            self.start = False
            print "OnStopWork",
            # 取消屏蔽编辑
            Frame.am_end.Enable(True)
            Frame.am_start.Enable(True)
            Frame.pm_end.Enable(True)
            Frame.pm_start.Enable(True)
            Frame.period.Enable(True)
            Frame.start_toggle.SetLabel("开始")
            Frame.am_lists.SetLabel('')
            Frame.pm_lists.SetLabel('')
            self.scheduler.remove_all_jobs()  # 停止所有的job


        else:
            self.start = True
            print "OnStartWor"
            # 屏蔽编辑k
            Frame.am_end.Enable(False)
            Frame.am_start.Enable(False)
            Frame.pm_end.Enable(False)
            Frame.pm_start.Enable(False)
            Frame.period.Enable(False)
            Frame.start_toggle.SetLabel("停止")

            Frame.am_lists.SetLabel()
            Frame.pm_lists.SetLabel()
            self.scheduler.add_job(myJob, trigger=IntervalTrigger(seconds=3))  # 开始所有的job

        pass

    def onReset(self, Frame):
        print "OnResetLastConf"
        if not Frame.dialog:
            Frame.dialog = MyDialog()
        Frame.dialog.Show()
        pass


def myJob():
    print "hello", datetime.datetime.now()
