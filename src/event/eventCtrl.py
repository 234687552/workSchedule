# -*- coding: cp936 -*-
'''
��������¼�����
'''
import datetime
import time
from src.scheduler.Scheduler import Scheduler
from apscheduler.triggers.interval import IntervalTrigger

from src.utils import ComputeDueTime


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
            Frame.reset.Enable(True)
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
            Frame.reset.Enable(False)
            Frame.start_toggle.SetLabel("ֹͣ")

            aheadTime = 5
            am_start, am_end, pm_start, pm_end, period = Frame.am_start.GetValue(), Frame.am_end.GetValue(), Frame.pm_start.GetValue(), Frame.pm_end.GetValue(), int(
                Frame.period.GetValue())
            am_lists, pm_lists = ComputeDueTime.getDueTime(am_start, am_end, pm_start, pm_end, period, aheadTime)
            temp = ''
            for i in range(len(am_lists)):
                temp += ComputeDueTime.TimeStamp2Str(am_lists[i], '%H:%M') + ' '
                am_lists[i] = ComputeDueTime.TimeStamp2Str(am_lists[i])
                # self.scheduler.add_job(self.showDialog, trigger=IntervalTrigger(seconds=3), args=[Frame])
            Frame.am_lists.SetLabel(temp)
            temp = ''
            for i in range(len(pm_lists)):
                temp += ComputeDueTime.TimeStamp2Str(pm_lists[i], '%H:%M') + ' '
                pm_lists[i] = ComputeDueTime.TimeStamp2Str(pm_lists[i])
                # self.scheduler.add_job(self.showDialog, trigger=IntervalTrigger(seconds=3), args=[Frame])
            Frame.pm_lists.SetLabel(temp)

            self.scheduler.add_job(self.showDialog, trigger=IntervalTrigger(seconds=3), args=[Frame])  # ��ʼ���е�job

        pass

    def onReset(self, Frame):
        print "OnResetLastConf"
        Frame.dialog.Show()
        pass

    def onDialogClose(self):
        self.dialogShow = False

    def showDialog(self, Frame):
        if not Frame.dialog.Shown:
            Frame.dialog.Show()
