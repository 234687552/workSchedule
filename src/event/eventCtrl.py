# -*- coding: cp936 -*-
'''
��������¼�����
'''
import datetime

from src.scheduler.Scheduler import Scheduler
from apscheduler.triggers.interval import IntervalTrigger
from src.wxpython.MyDialog import MyDialog



class EventCtrl(object):
    # ���徲̬����ʵ��
    __singleton = None

    def __init__(self):
        self.start = False  # Ĭ����û��ʼ
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
            # ȡ�����α༭
            Frame.am_end.Enable(True)
            Frame.am_start.Enable(True)
            Frame.pm_end.Enable(True)
            Frame.pm_start.Enable(True)
            Frame.period.Enable(True)
            Frame.start_toggle.SetLabel("��ʼ")
            Frame.am_lists.SetLabel('')
            Frame.pm_lists.SetLabel('')
            self.scheduler.remove_all_jobs()  # ֹͣ���е�job


        else:
            self.start = True
            print "OnStartWor"
            # ���α༭k
            Frame.am_end.Enable(False)
            Frame.am_start.Enable(False)
            Frame.pm_end.Enable(False)
            Frame.pm_start.Enable(False)
            Frame.period.Enable(False)
            Frame.start_toggle.SetLabel("ֹͣ")

            Frame.am_lists.SetLabel()
            Frame.pm_lists.SetLabel()
            self.scheduler.add_job(myJob, trigger=IntervalTrigger(seconds=3))  # ��ʼ���е�job

        pass

    def onReset(self, Frame):
        print "OnResetLastConf"
        if not Frame.dialog:
            Frame.dialog = MyDialog()
        Frame.dialog.Show()
        pass


def myJob():
    print "hello", datetime.datetime.now()
