# -*- coding: cp936 -*-
import wx


class TaskBarIcon(wx.TaskBarIcon):
    ID_ABOUT = wx.NewId()  # 定义好菜单ID - HELLO
    ID_EXIT = wx.NewId()  # 定义好菜单ID - EXIT

    def __init__(self, frame):
        wx.TaskBarIcon.__init__(self)
        self.frame = frame
        self.SetIcon(wx.Icon(name='wx.ico', type=wx.BITMAP_TYPE_ICO), 'TaskBarIcon!')
        self.Bind(wx.EVT_TASKBAR_LEFT_DCLICK, self.OnTaskBarLeftDClick)  # 左键双击托盘事件

        self.Bind(wx.EVT_MENU, self.OnAbout, id=self.ID_ABOUT)  # 点击菜单about的事件
        self.Bind(wx.EVT_MENU, self.OnExit, id=self.ID_EXIT)  # 点击菜单exit的事件

    # override 创建托盘右击菜单
    def CreatePopupMenu(self):
        menu = wx.Menu()
        menu.Append(self.ID_ABOUT, '关于')
        menu.Append(self.ID_EXIT, '退出')
        return menu

    # 双击托盘事件
    def OnTaskBarLeftDClick(self, event):

        if self.frame.IsIconized():
            self.frame.Iconize(False)
        if not self.frame.IsShown():
            self.frame.Show(True)  # 显示软件
            self.frame.Raise()

    def OnAbout(self, event):
        wx.MessageBox('Copr. 2017 lzd', 'About')

    def OnExit(self, event):
        self.frame.taskBarIcon.Destroy()
        self.frame.Destroy()


# 面板布局格式
class Frame(wx.Frame):
    def __init__(
            self, parent=None, id=wx.ID_ANY, title='TaskBarIcon', pos=wx.DefaultPosition,
            size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE):
        wx.Frame.__init__(self, parent, id, title, pos, size, style)

        self.SetIcon(wx.Icon('wx.ico', wx.BITMAP_TYPE_ICO))  # 设置图标

        panel = wx.Panel(self, wx.ID_ANY)
        button = wx.Button(panel, wx.ID_ANY, 'Hide Frame')  #
        self.Bind(wx.EVT_BUTTON, self.OnHide, button)  # 把新建的按钮添加最小化事件

        self.Bind(wx.EVT_CLOSE, self.OnClose)  # 关闭按钮

        self.taskBarIcon = TaskBarIcon(self)  # 设置程序为托盘形式

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
