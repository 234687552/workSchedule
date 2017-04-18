# -*- coding: cp936 -*-
import wx
import wx.xrc
from TaskBarIcon import TaskBarIcon
from MyDialog import MyDialog

# ��岼�ָ�ʽ
from src.event.eventCtrl import EventCtrl


class MyFrame(wx.Frame):
    def __init__(
            self, parent=None, id=wx.ID_ANY, title='TaskBarIcon', pos=wx.DefaultPosition,
            size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE):
        wx.Frame.__init__(self, parent, id, title, pos, size, style)

        # add by wxFormBuilder ������������������  no modify by code
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        sbSizer1 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"ÿ�칤��ʱ��"), wx.VERTICAL)

        gSizer2 = wx.GridSizer(0, 4, 0, 0)

        self.m_staticText2 = wx.StaticText(sbSizer1.GetStaticBox(), wx.ID_ANY, u"����:", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        gSizer2.Add(self.m_staticText2, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.am_start = wx.TextCtrl(sbSizer1.GetStaticBox(), wx.ID_ANY, u"08:30", wx.DefaultPosition, wx.DefaultSize,
                                    wx.TE_CENTRE)
        gSizer2.Add(self.am_start, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText3 = wx.StaticText(sbSizer1.GetStaticBox(), wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize,
                                           0)
        self.m_staticText3.Wrap(-1)
        gSizer2.Add(self.m_staticText3, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.am_end = wx.TextCtrl(sbSizer1.GetStaticBox(), wx.ID_ANY, u"12:00", wx.DefaultPosition, wx.DefaultSize,
                                  wx.TE_CENTRE)
        gSizer2.Add(self.am_end, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText4 = wx.StaticText(sbSizer1.GetStaticBox(), wx.ID_ANY, u"����:", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)
        gSizer2.Add(self.m_staticText4, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.pm_start = wx.TextCtrl(sbSizer1.GetStaticBox(), wx.ID_ANY, u"13:30", wx.DefaultPosition, wx.DefaultSize,
                                    wx.TE_CENTRE)
        gSizer2.Add(self.pm_start, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText5 = wx.StaticText(sbSizer1.GetStaticBox(), wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize,
                                           0)
        self.m_staticText5.Wrap(-1)
        gSizer2.Add(self.m_staticText5, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.pm_end = wx.TextCtrl(sbSizer1.GetStaticBox(), wx.ID_ANY, u"18:00", wx.DefaultPosition, wx.DefaultSize,
                                  wx.TE_CENTRE)
        gSizer2.Add(self.pm_end, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        sbSizer1.Add(gSizer2, 1, wx.EXPAND, 5)

        bSizer1.Add(sbSizer1, 1, wx.EXPAND, 5)

        gSizer3 = wx.GridSizer(0, 3, 0, 0)

        self.m_staticText6 = wx.StaticText(self, wx.ID_ANY, u"ÿ�೤ʱ������(����)", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)
        gSizer3.Add(self.m_staticText6, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.period = wx.TextCtrl(self, wx.ID_ANY, u"60", wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT)
        gSizer3.Add(self.period, 0, wx.ALL | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText7 = wx.StaticText(self, wx.ID_ANY, u"min", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText7.Wrap(-1)
        gSizer3.Add(self.m_staticText7, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer1.Add(gSizer3, 1, wx.EXPAND, 5)

        remind_time = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"����ʱ��"), wx.VERTICAL)

        fgSizer4 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer4.AddGrowableCol(1)
        fgSizer4.AddGrowableRow(1)
        fgSizer4.SetFlexibleDirection(wx.BOTH)
        fgSizer4.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText16 = wx.StaticText(remind_time.GetStaticBox(), wx.ID_ANY, u"����:", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText16.Wrap(-1)
        fgSizer4.Add(self.m_staticText16, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.am_lists = wx.StaticText(remind_time.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                      wx.DefaultSize, 0)
        self.am_lists.Wrap(-1)
        fgSizer4.Add(self.am_lists, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText18 = wx.StaticText(remind_time.GetStaticBox(), wx.ID_ANY, u"����:", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText18.Wrap(-1)
        fgSizer4.Add(self.m_staticText18, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.pm_lists = wx.StaticText(remind_time.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                      wx.DefaultSize, 0)
        self.pm_lists.Wrap(-1)
        fgSizer4.Add(self.pm_lists, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        remind_time.Add(fgSizer4, 1, wx.EXPAND, 5)

        bSizer1.Add(remind_time, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        gSizer4 = wx.GridSizer(0, 2, 0, 0)

        self.reset = wx.Button(self, wx.ID_ANY, u"����", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer4.Add(self.reset, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.start_toggle = wx.Button(self, wx.ID_ANY, u"��ʼ", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer4.Add(self.start_toggle, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 5)

        bSizer1.Add(gSizer4, 0, wx.ALIGN_RIGHT, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.reset.Bind(wx.EVT_BUTTON, self.OnReset)
        self.start_toggle.Bind(wx.EVT_BUTTON, self.OnStartToggle)
        # �ǵ����������
        self.reset.Hide()
        # add by wxFormBuilder ������������������  no modify by code

        self.dialog = MyDialog()
        self.SetIcon(wx.Icon('.importance\loadIcon.ico', wx.BITMAP_TYPE_ICO))  # ����ͼ��

        self.Bind(wx.EVT_CLOSE, self.OnClose)  # �رհ�ť

        self.taskBarIcon = TaskBarIcon(self)  # ���ó���Ϊ������ʽ

        wx.Frame.SetMaxSize(self, size)  # ���ߴ�
        wx.Frame.SetMinSize(self, size)  # ��С�ߴ�

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    # ��������
    def OnReset(self, event):
        EventCtrl.getInstance().onReset(self)
        event.Skip()

    # �����ʼ
    def OnStartToggle(self, event):
        EventCtrl.getInstance().onStartToggle(self)
        event.Skip()

    def OnClose(self, event):
        self.Hide()
