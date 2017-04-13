# -*- coding: utf-8 -*-
# 此包作用是 因为pyinstaller + apscheduler  产生 的exe在win7不执行
# http://www.cnblogs.com/ginponson/p/6079928.html
# http://blog.csdn.net/u011962883/article/details/53436824
from PyInstaller.utils.hooks import copy_metadata

datas = copy_metadata('apscheduler')