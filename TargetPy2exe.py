#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '将TargetOpinionMain python项目转换为exe文件'
__author__ = 'lzd'
__email__ = ' '
"""
from PyInstaller.__main__ import run

if __name__ == '__main__':
    # opts = ['tuopan.py', '-F']
    # opts = ['tuopan.py', '-F', '-w']
    opts = ['tuopan.py', '-F', '-w', '--icon=wx.ico','--upx-dir','upx391w']
    run(opts)