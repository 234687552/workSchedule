# -*- coding: utf-8 -*-

import os
import shutil

import sys
import xlrd
import xlutils.copy
import xlwt

import time

from src.entity.ExcelData import ExcelData
from src.utils import ComputeDueTime


def ExcelStyle(name=u'宋体', height=220, frontColor=0, bold=False, isHorz=False, num_format='general', hasBorders=True):
    style = xlwt.XFStyle()  # 初始化样式
    style.num_format_str = num_format  # 数字格式

    font = xlwt.Font()  # 为样式创建字体
    font.name = name  # 'Times New Roman'
    font.bold = bold
    font.colour_index = frontColor
    font.height = height
    style.font = font

    if hasBorders:
        borders = xlwt.Borders()
        borders.top = 1
        borders.bottom = 1
        borders.left = 1
        borders.right = 1
        borders.bottom_colour = 0x3A
        style.borders = borders  # Add borders  to Style

    alignment = xlwt.Alignment()
    alignment.vert = xlwt.Alignment.VERT_CENTER  # 垂直居中
    if isHorz:
        alignment.horz = xlwt.Alignment.HORZ_CENTER  # 水平居中
    style.alignment = alignment

    return style


def writeExcel(todayFile, excelData):
    # 从某一cell开始往下搜索空闲的行，sheet 是xlrd.open_workbook().get_sheet的对象
    def findFreeCell(sheet, startX, startY):
        # sheet.cell(0,0).value  sheet.cell_value(0,1)
        x = startX
        while not sheet.cell_value(x, startY) == '':
            x += 1
        return x

    rb = xlrd.open_workbook(todayFile, formatting_info=True)
    wb = xlutils.copy.copy(rb)  # 获取可编辑的对象
    ws = wb.get_sheet(0)
    if not ws.name == time.strftime("%m月%d日").decode('utf-8', 'ignore'):
        ws.set_name(time.strftime("%m月%d日").decode('utf-8', 'ignore'))
        ws.write(1, 9, time.strftime("%Y-%m-%d").decode('utf-8', 'ignore'), ExcelStyle(hasBorders=False, bold=True))
    day = time.strftime("%Y-%m-%d ")  # 当天日期
    freeX = 3
    if ComputeDueTime.Str2TimeStamp(day + excelData.start) <= ComputeDueTime.Str2TimeStamp(day + '12:00'):
        freeX = findFreeCell(rb.sheet_by_index(0), 3, 2)  # 早上从3,3找往下找空闲的cell
    else:
        freeX = findFreeCell(rb.sheet_by_index(0), 11, 2)  # 下午从3,3找往下找空闲的cell

    if len(excelData.workType) > 0:
        ws.write(freeX, 2, excelData.workType.decode('utf-8', 'ignore'), ExcelStyle())  # 工作类型
    if len(excelData.content) > 0:
        ws.write(freeX, 3, excelData.content.decode('utf-8', 'ignore'), ExcelStyle())  # 具体内容
    if len(excelData.result) > 0:
        ws.write(freeX, 6, excelData.result.decode('utf-8', 'ignore'), ExcelStyle(isHorz=True))  # 输出结果
    if len(excelData.start) > 0 and len(excelData.end) > 0:
        startTimeStamp = ComputeDueTime.Str2TimeStamp(day + excelData.start)
        endTimeStamp = ComputeDueTime.Str2TimeStamp(day + excelData.end)
        duration = (endTimeStamp - startTimeStamp) / 60  # 单位从秒转分
        ws.write(freeX, 9, duration, ExcelStyle(isHorz=True))  # 耗时
    if len(excelData.remarks) > 0:
        ws.write(freeX, 10, excelData.remarks.decode('utf-8', 'ignore'), ExcelStyle())  # 备注

    ws.write(19, 9, xlwt.Formula('SUM(J4:J19)/60'), ExcelStyle(frontColor=2, bold=True, isHorz=True, num_format='0.00'))
    wb.save(todayFile)


def checkAndWriteExcel(excelData):
    reload(sys)  # 2
    sys.setdefaultencoding('utf-8')
    # rootPath = os.path.dirname(os.path.dirname(os.getcwd()))  # 程序所在更目录：当前目录的上一层的上一层
    rootPath = os.getcwd()  # 程序所在更目录：当前目录的上一层的上一层
    todayFile = os.path.join(rootPath, time.strftime("%m-%d") + ".xls")  # 保存文件的全路径
    if not os.path.exists(todayFile):
        # samplePath = os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), ".importance\sample.xls")  # 样本路径 当前目录的上一层的上一层
        samplePath = os.path.join(os.getcwd(), ".importance\sample.xls")  # 样本路径 当前目录的上一层的上一层
        shutil.copy(samplePath, todayFile)

    writeExcel(todayFile, excelData)


if __name__ == '__main__':
    checkAndWriteExcel(ExcelData("固定工作", "content", "result", "08:30", "09:30", "remarks"))
