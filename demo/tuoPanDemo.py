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
