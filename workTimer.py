# -*- coding: cp936 -*-
import datetime
import wx
import wx.xrc

from src.wxpython.MyFrame import MyFrame
from src.scheduler.Scheduler import Scheduler
from apscheduler.triggers.interval import IntervalTrigger


# 启动界面
def StartFrame():
    app = wx.App()
    frame = MyFrame(size=(513, 235))
    frame.Centre()
    frame.Show()
    app.MainLoop()


# 开始计划任务
def StartSchedule():
    scheduler = Scheduler.getInstance().getScheduler()
    scheduler.add_job(myJob, trigger=IntervalTrigger(seconds=3))


def myJob():
    print "hello", datetime.datetime.now()


if __name__ == '__main__':
    StartSchedule()
    StartFrame()  # 放在最后启动界面
