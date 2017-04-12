# -*- coding: cp936 -*-
import wx
import wx.xrc
from TaskBarIcon import TaskBarIcon
from MyDialog import MyDialog


# ��岼�ָ�ʽ
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

        self.m_staticText2 = wx.StaticText(sbSizer1.GetStaticBox(), wx.ID_ANY, u"����", wx.DefaultPosition,
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

        self.m_staticText4 = wx.StaticText(sbSizer1.GetStaticBox(), wx.ID_ANY, u"����", wx.DefaultPosition,
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

        gSizer5 = wx.GridSizer(0, 2, 0, 0)

        self.reset_last_cof = wx.Button(self, wx.ID_ANY, u"��������", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer5.Add(self.reset_last_cof, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.start_toggle = wx.Button(self, wx.ID_ANY, u"��ʼ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.start_toggle.SetDefault()
        gSizer5.Add(self.start_toggle, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 5)

        bSizer1.Add(gSizer5, 1, wx.ALIGN_RIGHT, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.reset_last_cof.Bind(wx.EVT_BUTTON, self.OnResetLastConf)
        self.start_toggle.Bind(wx.EVT_BUTTON, self.OnStartToggle)

        # add by wxFormBuilder ������������������  no modify by code
        self.dialog = None
        self.SetIcon(wx.Icon('loadIcon.ico', wx.BITMAP_TYPE_ICO))  # ����ͼ��

        self.Bind(wx.EVT_CLOSE, self.OnClose)  # �رհ�ť

        self.taskBarIcon = TaskBarIcon(self)  # ���ó���Ϊ������ʽ

        wx.Frame.SetMaxSize(self, size)  # ���ߴ�
        wx.Frame.SetMinSize(self, size)  # ��С�ߴ�
        self.start = False  # Ĭ����û��ʼ

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    # ��������
    def OnResetLastConf(self, event):
        print "OnResetLastConf"
        self.dialog = MyDialog()
        self.dialog.Show()
        event.Skip()

    # �����ʼ
    def OnStartToggle(self, event):
        if self.start:
            print "OnStopWork",
            # ȡ�����α༭
            self.am_end.Enable(True)
            self.am_start.Enable(True)
            self.pm_end.Enable(True)
            self.pm_start.Enable(True)
            self.period.Enable(True)
            self.start_toggle.SetLabel("ֹͣ")
            self.start = False
        else:
            print "OnStartWork"
            # ���α༭
            self.am_end.Enable(False)
            self.am_start.Enable(False)
            self.pm_end.Enable(False)
            self.pm_start.Enable(False)
            self.period.Enable(False)
            self.start_toggle.SetLabel("��ʼ")
            self.start = True

        event.Skip()

    def OnHide(self, event):
        self.Hide()

    def OnClose(self, event):
        self.Hide()
