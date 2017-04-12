# -*- coding: utf-8 -*-
import time


def getFileName():
    # time.strftime("%W") 一年中的第几周
    return "%s周员工工作日志-工程部-.xls"%time.strftime("%W")


def getSheetName():
    return time.strftime("%m月%d日 ")


if __name__ == '__main__':
    print getSheetName()
    print getFileName()
