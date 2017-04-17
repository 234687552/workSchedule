# -*- coding: cp936 -*-
'''
软件所有事件控制
'''
import datetime
import time
from src.scheduler.Scheduler import Scheduler
from apscheduler.triggers.interval import IntervalTrigger

from src.utils import ComputeDueTime


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
            Frame.reset.Enable(True)
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
            Frame.reset.Enable(False)
            Frame.start_toggle.SetLabel("停止")

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

            self.scheduler.add_job(self.showDialog, trigger=IntervalTrigger(seconds=3), args=[Frame])  # 开始所有的job

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
