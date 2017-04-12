# -*- coding: cp936 -*-
import wx
import wx.xrc


# ���̿���
class TaskBarIcon(wx.TaskBarIcon):
    ID_MEMO = wx.NewId()  # ����ò˵�ID - ����
    ID_ABOUT = wx.NewId()  # ����ò˵�ID - ����
    ID_EXIT = wx.NewId()  # ����ò˵�ID - EXIT

    def __init__(self, frame):
        wx.TaskBarIcon.__init__(self)
        self.frame = frame
        self.SetIcon(wx.Icon(name='loadIcon.ico', type=wx.BITMAP_TYPE_ICO), 'TaskBarIcon!')
        self.Bind(wx.EVT_TASKBAR_LEFT_DCLICK, self.OnTaskBarLeftDClick)  # ���˫�������¼�

        self.Bind(wx.EVT_MENU, self.OnAbout, id=self.ID_ABOUT)  # ����˵�about���¼�
        self.Bind(wx.EVT_MENU, self.OnExit, id=self.ID_EXIT)  # ����˵�exit���¼�

    # override ���������һ��˵�
    def CreatePopupMenu(self):
        menu = wx.Menu()
        menu.Append(self.ID_MEMO, '����')
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
        # �رնԻ���
        if self.frame.dialog :
            self.frame.dialog.Destroy()

        # �ر�����
        self.frame.taskBarIcon.Destroy()

        # �رձ���
        self.frame.Destroy()
