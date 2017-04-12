#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '将TargetOpinionMain python项目转换为exe文件'
__author__ = 'lzd'
__email__ = ' '
"""
from PyInstaller.__main__ import run

if __name__ == '__main__':
    # opts = ['workTimer.py', '-F']
    # opts = ['workTimer.py', '-F', '-w']
    opts = ['workTimer.py', '-F', '-w', '--icon=loadIcon.ico', '--upx-dir', 'upx391w']
    run(opts)
