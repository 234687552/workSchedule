# -*- coding: cp936 -*-
import wx


class TaskBarIcon(wx.TaskBarIcon):
    ID_ABOUT = wx.NewId()  # ����ò˵�ID - HELLO
    ID_EXIT = wx.NewId()  # ����ò˵�ID - EXIT

    def __init__(self, frame):
        wx.TaskBarIcon.__init__(self)
        self.frame = frame
        self.SetIcon(wx.Icon(name='wx.ico', type=wx.BITMAP_TYPE_ICO), 'TaskBarIcon!')
        self.Bind(wx.EVT_TASKBAR_LEFT_DCLICK, self.OnTaskBarLeftDClick)  # ���˫�������¼�

        self.Bind(wx.EVT_MENU, self.OnAbout, id=self.ID_ABOUT)  # ����˵�about���¼�
        self.Bind(wx.EVT_MENU, self.OnExit, id=self.ID_EXIT)  # ����˵�exit���¼�

    # override ���������һ��˵�
    def CreatePopupMenu(self):
        menu = wx.Menu()
        menu.Append(self.ID_ABOUT, '����')
        menu.Append(self.ID_EXIT, '�˳�')
        return menu

    # ˫�������¼�
    def OnTaskBarLeftDClick(self, event):

        if self.frame.IsIconized():
            self.frame.Iconize(False)
        if not self.frame.IsShown():
            self.frame.Show(True)  # ��ʾ���
            self.frame.Raise()

    def OnAbout(self, event):
        wx.MessageBox('Copr. 2017 lzd', 'About')

    def OnExit(self, event):
        self.frame.taskBarIcon.Destroy()
        self.frame.Destroy()


# ��岼�ָ�ʽ
class Frame(wx.Frame):
    def __init__(
            self, parent=None, id=wx.ID_ANY, title='TaskBarIcon', pos=wx.DefaultPosition,
            size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE):
        wx.Frame.__init__(self, parent, id, title, pos, size, style)

        self.SetIcon(wx.Icon('wx.ico', wx.BITMAP_TYPE_ICO))  # ����ͼ��

        panel = wx.Panel(self, wx.ID_ANY)
        button = wx.Button(panel, wx.ID_ANY, 'Hide Frame')  #
        self.Bind(wx.EVT_BUTTON, self.OnHide, button)  # ���½��İ�ť�����С���¼�

        self.Bind(wx.EVT_CLOSE, self.OnClose)  # �رհ�ť

        self.taskBarIcon = TaskBarIcon(self)  # ���ó���Ϊ������ʽ

        # add by wxFormBuilder ������������������  no modify by code
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        fgSizer1 = wx.FlexGridSizer(0, 1, 0, 0)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        sbSizer3 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"ÿ�칤��ʱ��:"), wx.VERTICAL)

        gSizer1 = wx.GridSizer(0, 4, 0, 0)

        self.m_staticText8 = wx.StaticText(sbSizer3.GetStaticBox(), wx.ID_ANY, u"����", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText8.Wrap(-1)
        gSizer1.Add(self.m_staticText8, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_textCtrl29 = wx.TextCtrl(sbSizer3.GetStaticBox(), wx.ID_ANY, u"08:30", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        gSizer1.Add(self.m_textCtrl29, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_staticText9 = wx.StaticText(sbSizer3.GetStaticBox(), wx.ID_ANY, u"to", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText9.Wrap(-1)
        gSizer1.Add(self.m_staticText9, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_textCtrl30 = wx.TextCtrl(sbSizer3.GetStaticBox(), wx.ID_ANY, u"12:00", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        gSizer1.Add(self.m_textCtrl30, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_staticText10 = wx.StaticText(sbSizer3.GetStaticBox(), wx.ID_ANY, u"����", wx.DefaultPosition,
                                            wx.DefaultSize,
                                            0)
        self.m_staticText10.Wrap(-1)
        gSizer1.Add(self.m_staticText10, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_textCtrl31 = wx.TextCtrl(sbSizer3.GetStaticBox(), wx.ID_ANY, u"13:30", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        gSizer1.Add(self.m_textCtrl31, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_staticText11 = wx.StaticText(sbSizer3.GetStaticBox(), wx.ID_ANY, u"to", wx.DefaultPosition,
                                            wx.DefaultSize,
                                            0)
        self.m_staticText11.Wrap(-1)
        gSizer1.Add(self.m_staticText11, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_textCtrl32 = wx.TextCtrl(sbSizer3.GetStaticBox(), wx.ID_ANY, u"18:00", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        gSizer1.Add(self.m_textCtrl32, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        sbSizer3.Add(gSizer1, 1, wx.EXPAND, 5)

        fgSizer1.Add(sbSizer3, 1, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 5)

        gSizer2 = wx.GridSizer(0, 3, 0, 0)

        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY, u"ÿ�೤ʱ������(����):", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)
        gSizer2.Add(self.m_staticText5, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_textCtrl25 = wx.TextCtrl(self, wx.ID_ANY, u"60", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer2.Add(self.m_textCtrl25, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_staticText6 = wx.StaticText(self, wx.ID_ANY, u"min", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)
        gSizer2.Add(self.m_staticText6, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        fgSizer1.Add(gSizer2, 1, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 5)

        gSizer3 = wx.GridSizer(0, 1, 0, 0)

        self.m_button3 = wx.Button(self, wx.ID_ANY, u"��ʼ", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer3.Add(self.m_button3, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        fgSizer1.Add(gSizer3, 1, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.SetSizer(fgSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

    def OnHide(self, event):
        self.Hide()

    def OnClose(self, event):
        self.Hide()


def TestFrame():
    app = wx.App()
    frame = Frame(size=(640, 480))
    frame.Centre()
    frame.Show()
    app.MainLoop()


if __name__ == '__main__':
    TestFrame()
