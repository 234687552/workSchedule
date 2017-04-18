# -*- coding: cp936 -*-
import wx
import wx.xrc
from src.event.eventCtrl import EventCtrl


class MyDialog(wx.Dialog):
    def __init__(self):
        wx.Dialog.__init__(self, parent=None, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                           size=wx.Size(558, 230), style=wx.DEFAULT_DIALOG_STYLE | wx.STAY_ON_TOP)
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        gSizer4 = wx.GridSizer(0, 1, 0, 0)

        gSizer5 = wx.GridSizer(0, 4, 0, 0)

        self.m_staticText17 = wx.StaticText(self, wx.ID_ANY, u"工作类型:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText17.Wrap(-1)
        gSizer5.Add(self.m_staticText17, 0, wx.ALL, 5)

        self.m_staticText18 = wx.StaticText(self, wx.ID_ANY, u"具体内容:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText18.Wrap(-1)
        gSizer5.Add(self.m_staticText18, 0, wx.ALL, 5)

        self.m_staticText19 = wx.StaticText(self, wx.ID_ANY, u"输出结果:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText19.Wrap(-1)
        gSizer5.Add(self.m_staticText19, 0, wx.ALL, 5)

        self.m_staticText20 = wx.StaticText(self, wx.ID_ANY, u"备注:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText20.Wrap(-1)
        gSizer5.Add(self.m_staticText20, 0, wx.ALL, 5)

        work_typeChoices = [u"固定工作", u"非固定工作"]
        self.work_type = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, work_typeChoices, 0)
        self.work_type.SetSelection(0)
        gSizer5.Add(self.work_type, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.work_content = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TE_MULTILINE)
        self.work_content.SetMinSize(wx.Size(-1, 100))

        gSizer5.Add(self.work_content, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_BOTTOM, 5)

        self.work_result = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                       wx.TE_MULTILINE)
        self.work_result.SetMinSize(wx.Size(-1, 100))

        gSizer5.Add(self.work_result, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_BOTTOM, 5)

        self.work_remarks = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TE_MULTILINE)
        self.work_remarks.SetMinSize(wx.Size(-1, 100))

        gSizer5.Add(self.work_remarks, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_BOTTOM, 5)

        self.m_staticText171 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText171.Wrap(-1)
        gSizer5.Add(self.m_staticText171, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.duration = wx.StaticText(self, wx.ID_ANY, u"08:30-09:30", wx.DefaultPosition, wx.DefaultSize, 0)
        self.duration.Wrap(-1)
        self.duration.SetFont(wx.Font(20, 70, 90, 92, False, wx.EmptyString))

        gSizer5.Add(self.duration, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_button1 = wx.Button(self, wx.ID_ANY, u"保存", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer5.Add(self.m_button1, 0, wx.ALL | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_button2 = wx.Button(self, wx.ID_ANY, u"下一周期再说", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer5.Add(self.m_button2, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        gSizer4.Add(gSizer5, 1, wx.EXPAND, 5)

        self.SetSizer(gSizer4)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.m_button1.Bind(wx.EVT_BUTTON, self.onSave)
        self.m_button2.Bind(wx.EVT_BUTTON, self.onNext)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def OnClose(self, event):
        # self.Destroy() #关闭对话框

        EventCtrl.getInstance().onDialogNext(self)
        event.Skip()

    def onSave(self, event):
        EventCtrl.getInstance().onDialogSave(self)
        event.Skip()

    def onNext(self, event):
        EventCtrl.getInstance().onDialogNext(self)
        event.Skip()

    def SetTimeLabelAndReset(self, time):
        self.duration.SetLabel(time)
        self.work_content.SetValue("")
        self.work_result.SetValue("")
        self.work_remarks.SetValue("")
        pass
