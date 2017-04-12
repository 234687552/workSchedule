# -*- coding: cp936 -*-
import datetime
import wx
import wx.xrc

from src.wxpython.MyFrame import MyFrame
from src.scheduler.Scheduler import Scheduler

# ��������
def StartFrame():
    app = wx.App()
    frame = MyFrame(size=(513, 235))
    frame.Centre()
    frame.Show()
    app.MainLoop()


# ��ʼ�ƻ�����
def StartSchedule():
    scheduler = Scheduler.getInstance().getScheduler()
    scheduler.add_job(myJob, 'interval', seconds=3)


def myJob():
    print "hello", datetime.datetime.now()


if __name__ == '__main__':
    StartSchedule()
    StartFrame()  # ���������������
