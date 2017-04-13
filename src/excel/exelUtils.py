# -*- coding: utf-8 -*-
import os
import shutil

import time
import xlrd
import xlwt
from xlutils import copy
from xlwt import *

if __name__ == '__main__':
    file_name = time.strftime("%W") + ".xls"  # shutil.copy遇到中文名称会报错 所以取这一年第几周 作为文件名  result:15.xls
    full_filename = os.path.join(os.getcwd(), file_name)
    samplePath = os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), ".importance\sample.xls")  # 样本路径
    print  samplePath
    # 判断文件是否存在
    if not os.path.isfile(file_name):
        shutil.copy(samplePath, full_filename)

    workbook = xlrd.open_workbook(file_name)
    print workbook.sheet_names()
    try:
        sampleSheet = workbook.sheet_by_name(u'sample')  # 打开样本sheet
    except Exception as  e:
        print e

    try:
        todaySheet = workbook.sheet_by_name(time.strftime("%m月%d日").decode('utf-8', 'ignore'))
    except Exception as e:  # 没有当天的sheet
        todaySheet = copy.copy(sampleSheet)
        workbook._Workbook__worksheets.append(todaySheet)
        append_index = len(workbook._Workbook__worksheets) - 1
        workbook.set_active_sheet(append_index)
        workbook.get_sheet(append_index).set_name(time.strftime("%m月%d日").decode('utf-8', 'ignore'))


'''
workbook     == book in use
source_index == index of sheet you want to copy (0 start)
new_name     == name of new copied sheet
'''


def copy_sheet(workbook, source_index, new_name):
    new_sheet = copy.copy(workbook.get_sheet(source_index))

    workbook._Workbook__worksheets.append(new_sheet)

    append_index = len(workbook._Workbook__worksheets) - 1

    workbook.set_active_sheet(append_index)

    workbook.get_sheet(append_index).set_name(new_name)
