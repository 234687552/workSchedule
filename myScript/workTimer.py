# -*- coding: cp936 -*-
import wx
import wx.xrc

from src.wxpython.MyFrame import MyFrame


def TestFrame():
    app = wx.App()
    frame = MyFrame(size=(513, 235))
    frame.Centre()
    frame.Show()
    app.MainLoop()


if __name__ == '__main__':
    TestFrame()
