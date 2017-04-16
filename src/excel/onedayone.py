# -*- coding: utf-8 -*-

import os
import shutil
import xlrd
import xlutils.copy
import xlwt

import time

from src.entity.ExcelData import ExcelData


def ExcelStyle(name=u'宋体', height=220, bold=False):
    style = xlwt.XFStyle()  # 初始化样式

    font = xlwt.Font()  # 为样式创建字体
    font.name = name  # 'Times New Roman'
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font

    alignment = xlwt.Alignment()
    alignment.vert = xlwt.Alignment.VERT_CENTER  # 垂直居中
    style.alignment = alignment
    return style


def writeExcel(todayFile, excelData):
    rb = xlrd.open_workbook(todayFile, formatting_info=True)
    wb = xlutils.copy.copy(rb)  # 获取可编辑的对象
    ws = wb.get_sheet(0)
    if not ws.name == time.strftime("%m月%d日").decode('utf-8', 'ignore'):
        ws.set_name(time.strftime("%m月%d日").decode('utf-8', 'ignore'))

    ws.write(3, 3, 'hehe', ExcelStyle())
    wb.save(todayFile)
    pass


if __name__ == '__main__':
    rootPath = os.path.dirname(os.path.dirname(os.getcwd()))  # 程序所在更目录：当前目录的上一层的上一层
    todayFile = os.path.join(rootPath, time.strftime("%m-%d") + ".xls")  # 保存文件的全路径
    if not os.path.exists(todayFile):
        samplePath = os.path.join(
            os.path.dirname(os.path.dirname(os.getcwd())), ".importance\sample.xls")  # 样本路径 当前目录的上一层的上一层
        shutil.copy(samplePath, todayFile)

    writeExcel(todayFile, ExcelData("1", "1", "1", "1"))
