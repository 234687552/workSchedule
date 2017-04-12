# -*- coding: cp936 -*-
import wx
import wx.xrc


# 托盘控制
class TaskBarIcon(wx.TaskBarIcon):
    ID_MEMO = wx.NewId()  # 定义好菜单ID - 备忘
    ID_ABOUT = wx.NewId()  # 定义好菜单ID - 关于
    ID_EXIT = wx.NewId()  # 定义好菜单ID - EXIT

    def __init__(self, frame):
        wx.TaskBarIcon.__init__(self)
        self.frame = frame
        self.SetIcon(wx.Icon(name='loadIcon.ico', type=wx.BITMAP_TYPE_ICO), 'TaskBarIcon!')
        self.Bind(wx.EVT_TASKBAR_LEFT_DCLICK, self.OnTaskBarLeftDClick)  # 左键双击托盘事件

        self.Bind(wx.EVT_MENU, self.OnAbout, id=self.ID_ABOUT)  # 点击菜单about的事件
        self.Bind(wx.EVT_MENU, self.OnExit, id=self.ID_EXIT)  # 点击菜单exit的事件

    # override 创建托盘右击菜单
    def CreatePopupMenu(self):
        menu = wx.Menu()
        menu.Append(self.ID_MEMO, '备忘')
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
        # 关闭对话框
        if self.frame.dialog :
            self.frame.dialog.Destroy()

        # 关闭托盘
        self.frame.taskBarIcon.Destroy()

        # 关闭本体
        self.frame.Destroy()
