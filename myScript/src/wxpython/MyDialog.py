# -*- coding: cp936 -*-
import wx
import wx.xrc


class MyDialog(wx.Dialog):
    def __init__(self):
        wx.Dialog.__init__(self, parent=None, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                           size=wx.DefaultSize, style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        fgSizer2 = wx.FlexGridSizer(0, 1, 0, 0)
        fgSizer2.SetFlexibleDirection(wx.BOTH)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.workPeriod = wx.StaticText(self, wx.ID_ANY, u"08:30-09:30", wx.DefaultPosition, wx.DefaultSize, 0)
        self.workPeriod.Wrap(-1)
        fgSizer2.Add(self.workPeriod, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        fgSizer3 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer3.SetFlexibleDirection(wx.BOTH)
        fgSizer3.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText12 = wx.StaticText(self, wx.ID_ANY, u"这段时间做了什么:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText12.Wrap(-1)
        fgSizer3.Add(self.m_staticText12, 0, wx.ALL, 5)

        self.m_staticText14 = wx.StaticText(self, wx.ID_ANY, u"输出结果为:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText14.Wrap(-1)
        fgSizer3.Add(self.m_staticText14, 0, wx.ALL, 5)

        self.m_textCtrl14 = wx.TextCtrl(self, wx.ID_ANY, u"大法师法撒旦极乐空间O(∩_∩打)O好的算分散", wx.DefaultPosition, wx.DefaultSize,
                                        wx.TE_MULTILINE)
        self.m_textCtrl14.SetMinSize(wx.Size(150, 150))

        fgSizer3.Add(self.m_textCtrl14, 0, wx.ALL, 5)

        self.m_textCtrl15 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TE_MULTILINE)
        self.m_textCtrl15.SetMinSize(wx.Size(-1, 150))

        fgSizer3.Add(self.m_textCtrl15, 0, wx.ALL, 5)

        fgSizer2.Add(fgSizer3, 1, wx.EXPAND, 5)

        gSizer4 = wx.GridSizer(0, 2, 0, 0)

        self.m_button8 = wx.Button(self, wx.ID_ANY, u"保存", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer4.Add(self.m_button8, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_button9 = wx.Button(self, wx.ID_ANY, u"下一周期再说", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer4.Add(self.m_button9, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        fgSizer2.Add(gSizer4, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.SetSizer(fgSizer2)
        self.Layout()
        fgSizer2.Fit(self)

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.OnClose)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def OnClose(self, event):
        self.Destroy() #关闭对话框
        event.Skip()
