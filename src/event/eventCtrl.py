# -*- coding: cp936 -*-
'''
��������¼�����
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
    # ���徲̬����ʵ��
    __singleton = None

    def __init__(self):
        self.start = False  # Ĭ����û��ʼ
        self.scheduler = Scheduler.getInstance().getScheduler()
        self.lastSaveTime = ''  # dialog������水ť�� ��¼��ǰʱ��
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
            Frame.am_lists.SetLabel(temp)
            temp = ''
            for i in range(len(pm_lists)):
                temp += ComputeDueTime.TimeStamp2Str(pm_lists[i], '%H:%M') + ' '
                pm_lists[i] = ComputeDueTime.TimeStamp2Str(pm_lists[i])  # Ĭ�ϸ�ʽ��"%Y-%m-%d %H:%M:%S"
            Frame.pm_lists.SetLabel(temp)

            for i in range(len(am_lists)):
                print am_lists[i]
                self.scheduler.add_job(self.showDialog, trigger=DateTrigger(run_date=am_lists[i]),
                                       args=[Frame, am_lists, i])  # ��Ӷ�ʱ����
            for i in range(len(pm_lists)):
                print pm_lists[i]
                self.scheduler.add_job(self.showDialog, trigger=DateTrigger(run_date=pm_lists[i]),
                                       args=[Frame, pm_lists, i])  # ��Ӷ�ʱ����

        pass

    def onReset(self, Frame):
        print "OnResetLastConf"
        Frame.dialog.Show()
        pass

    def showDialog(self, Frame, lists, index):
        print 'show dialog'

        if not Frame.dialog.m_button2.Shown:
            Frame.dialog.m_button2.Show()  # ��ʾnext��ť

        isAm = ComputeDueTime.Str2TimeStamp(lists[0], "%Y-%m-%d %H:%M:%S") <= ComputeDueTime.Str2TimeStamp(
            time.strftime("%Y-%m-%d ") + '12:00')  # �Ƿ�Ϊ����

        # list[i]��ʽ "%Y-%m-%d %H:%M:%S"
        durationEnd = ComputeDueTime.TimeStamp2Str(
            ComputeDueTime.Str2TimeStamp(lists[index], "%Y-%m-%d %H:%M:%S"), '%H:%M')  # "%Y-%m-%d %H:%M:%S" ת'%H:%M'��ʽ
        print  self.lastSaveTime
        if not len(self.lastSaveTime) > 0 or index == 0:
            self.lastSaveTime = Frame.am_start.GetValue() if isAm else Frame.pm_start.GetValue()
        durationStart = self.lastSaveTime

        if index == len(lists) - 1:  # ���ϻ�����������һ������:
            Frame.dialog.m_button2.Hide()  # ����next��ť
            durationEnd = Frame.am_end.GetValue() if isAm else Frame.pm_end.GetValue()

        Frame.dialog.SetTimeLabelAndReset(durationStart + '-' + durationEnd)

        if not Frame.dialog.Shown:
            Frame.dialog.Show()

    def onDialogSave(self, dialog):
        # print 'dialog save'
        dialog.Hide()  # ���ضԻ���

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
        dialog.Hide()  # ���ضԻ���
        pass
