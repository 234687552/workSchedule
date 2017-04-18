# -*- coding: cp936 -*-
'''
软件所有事件控制
'''
import datetime
import time

from src.entity.ExcelData import ExcelData
from src.excel import excelUtils
from src.scheduler.Scheduler import Scheduler
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.date import DateTrigger

from src.utils import ComputeDueTime


class EventCtrl(object):
    # 定义静态变量实例
    __singleton = None

    def __init__(self):
        self.start = False  # 默认是没开始
        self.scheduler = Scheduler.getInstance().getScheduler()
        self.lastSaveTime = ''  # dialog点击保存按钮后 记录当前时间
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
            Frame.am_lists.SetLabel(temp)
            temp = ''
            for i in range(len(pm_lists)):
                temp += ComputeDueTime.TimeStamp2Str(pm_lists[i], '%H:%M') + ' '
                pm_lists[i] = ComputeDueTime.TimeStamp2Str(pm_lists[i])  # 默认格式："%Y-%m-%d %H:%M:%S"
            Frame.pm_lists.SetLabel(temp)

            for i in range(len(am_lists)):
                print am_lists[i]
                self.scheduler.add_job(self.showDialog, trigger=DateTrigger(run_date=am_lists[i]),
                                       args=[Frame, am_lists, i])  # 添加定时任务
            for i in range(len(pm_lists)):
                print pm_lists[i]
                self.scheduler.add_job(self.showDialog, trigger=DateTrigger(run_date=pm_lists[i]),
                                       args=[Frame, pm_lists, i])  # 添加定时任务

        pass

    def onReset(self, Frame):
        print "OnResetLastConf"
        Frame.dialog.Show()
        pass

    def showDialog(self, Frame, lists, index):
        print 'show dialog'

        if not Frame.dialog.m_button2.Shown:
            Frame.dialog.m_button2.Show()  # 显示next按钮

        isAm = ComputeDueTime.Str2TimeStamp(lists[0], "%Y-%m-%d %H:%M:%S") <= ComputeDueTime.Str2TimeStamp(
            time.strftime("%Y-%m-%d ") + '12:00')  # 是否为早上

        # list[i]格式 "%Y-%m-%d %H:%M:%S"
        durationEnd = ComputeDueTime.TimeStamp2Str(
            ComputeDueTime.Str2TimeStamp(lists[index], "%Y-%m-%d %H:%M:%S"), '%H:%M')  # "%Y-%m-%d %H:%M:%S" 转'%H:%M'格式
        print  self.lastSaveTime
        if not len(self.lastSaveTime) > 0 or index == 0:
            self.lastSaveTime = Frame.am_start.GetValue() if isAm else Frame.pm_start.GetValue()
        durationStart = self.lastSaveTime

        if index == len(lists) - 1:  # 早上或者下午的最后一条提醒:
            Frame.dialog.m_button2.Hide()  # 隐藏next按钮
            durationEnd = Frame.am_end.GetValue() if isAm else Frame.pm_end.GetValue()

        Frame.dialog.SetTimeLabelAndReset(durationStart + '-' + durationEnd)

        if not Frame.dialog.Shown:
            Frame.dialog.Show()

    def onDialogSave(self, dialog):
        # print 'dialog save'
        dialog.Hide()  # 隐藏对话框

        workType = dialog.work_type.StringSelection
        workContent = dialog.work_content.GetValue()
        workResult = dialog.work_result.GetValue()
        workRemarks = dialog.work_remarks.GetValue()
        workStart = dialog.duration.GetLabel().split('-')[0]
        workEnd = dialog.duration.GetLabel().split('-')[-1]
        self.lastSaveTime = workEnd

        print workType, workContent, workResult, workRemarks, workStart, workEnd
        excelData = ExcelData(workType=workType, content=workContent, result=workResult, remarks=workRemarks,
                              start=workStart, end=workEnd)
        excelUtils.checkAndWriteExcel(excelData)
        pass

    def onDialogNext(self, dialog):
        # print 'dialog next or close'
        dialog.Hide()  # 隐藏对话框
        pass
