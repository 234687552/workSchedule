# -*- coding: utf-8 -*-
from copy import deepcopy

import time
import os
import shutil

import xlrd
import xlutils.copy
import xlwt

from src.entity import ExcelData
from src.entity.ReturnInfo import ReturnInfo


# 修改值


def setOutCell(outSheet, col, row, value):
    """ Change cell value without changing formatting. """

    def _getOutCell(outSheet, colIndex, rowIndex):
        """ HACK: Extract the internal xlwt cell representation. """
        row = outSheet._Worksheet__rows.get(rowIndex)
        if not row: return None

        cell = row._Row__cells.get(colIndex)
        return cell

    # HACK to retain cell style.
    previousCell = _getOutCell(outSheet, col, row)
    # END HACK, PART I

    outSheet.write(row, col, value)

    # HACK, PART II
    if previousCell:
        newCell = _getOutCell(outSheet, col, row)
        if newCell:
            newCell.xf_idx = previousCell.xf_idx
            # END HACK


'''
# 使用范例:copySheet('test.xls', 'sample', 'fsdsa','test.xls')
把excel的原有一个sheet复制并重命名
'''


def copySheet(fileName, sourceSheetName, newSheetName, outFile):
    rb = xlrd.open_workbook(fileName, formatting_info=True)
    sheets = rb.sheets()  # 所有的sheets
    sourceSheetIndex = None
    newSheetIndex = None
    for i in range(len(sheets)):
        if sourceSheetName == sheets[i].name:
            sourceSheetIndex = i
        if newSheetName == sheets[i].name:
            newSheetIndex = i

    if (sourceSheetIndex):
        msg = '文件没有该名称的sheet:%s' % sourceSheetName
        return ReturnInfo(-1, msg)
    if (newSheetIndex):
        msg = '文件已经包含该名称的sheet:%s' % newSheetName
        return ReturnInfo(-1, msg)

    # 以下为正常情况逻辑
    wb = xlutils.copy.copy(rb)  # 获取可编辑的对象

    newSheet = deepcopy(wb.get_sheet(sourceSheetIndex))  # 用deepcopy防止对象是同一个
    newSheet.set_name(newSheetName)

    wb._Workbook__worksheets.append(newSheet)
    wb.set_active_sheet(0)
    wb.save(outFile)
    return ReturnInfo(1, "succeed")


def writeExcel(fileName, sheetName, excelData):
    if not os.path.exists(fileName):
        samplePath = os.path.join(
            os.path.dirname(os.path.dirname(os.getcwd())), ".importance\sample.xls")  # 样本路径 当前目录的上一层的上一层
        todaySheetName = time.strftime("%m月%d日")
        # copySheet(samplePath, 'sample', todaySheetName.decode('utf-8', 'ignore'), fileName)  # 没有就把样本拷贝过来
        copySheet(samplePath, 'sample', todaySheetName.decode('utf-8', 'ignore'), fileName)  # 没有就把样本拷贝过来

    rb = xlrd.open_workbook(fileName, formatting_info=True)

    wb = xlutils.copy.copy(rb)
    worksheet = wb.get_sheet(0)
    worksheet.write(0, 0, "hello")
    setOutCell(worksheet, 1, 2, 'sfa')
    wb.save(fileName)


writeExcel('tt.xls', 'sample', None)

# if __name__ == '__main__':
#
#     file_name = time.strftime("%W") + ".xls"  # shutil.copy遇到中文名称会报错 所以取这一年第几周 作为文件名  result:15.xls
#     full_filename = os.path.join(os.getcwd(), file_name)
#     samplePath = os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), ".importance\sample.xls")  # 样本路径
#     print  samplePath
#     # 判断这周的文件是否存在
#     if not os.path.isfile(file_name):
#         shutil.copy(samplePath, full_filename)  # 没有就把样本拷贝过来
#
#     workbook = xlrd.open_workbook(full_filename)
#     print workbook.sheet_names()
#     try:
#         sampleSheet = workbook.sheet_by_name(u'sample')  # 打开样本sheet
#     except Exception as  e:
#         print e
#
#     try:
#         todaySheet = workbook.sheet_by_name(time.strftime("%m月%d日").decode('utf-8', 'ignore'))
#     except Exception as e:  # 没有当天的sheet
#         todaySheet = copy.copy(sampleSheet)
#         workbook._Workbook__worksheets.append(todaySheet)
#         append_index = len(workbook._Workbook__worksheets) - 1
#         workbook.set_active_sheet(append_index)
#         workbook.get_sheet(append_index).set_name(time.strftime("%m月%d日").decode('utf-8', 'ignore'))
