# -*- coding: cp936 -*-
import datetime
import wx
import wx.xrc


from src.wxpython.MyFrame import MyFrame


# 启动界面
def StartFrame():
    app = wx.App()
    frame = MyFrame(size=(500, 341))
    frame.Centre()
    frame.Show()
    app.MainLoop()


if __name__ == '__main__':
    StartFrame()  # 放在最后启动界面
