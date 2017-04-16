# -*- coding: utf-8 -*-
import os

import xlrd
import xlutils.copy
import xlwt
import time


def read_excel():
    # 打开文件
    workbook = xlrd.open_workbook(r'tt.xls')
    # 获取所有sheet
    print workbook.sheet_names()  # [u'sheet1', u'sheet2']
    sheet2_name = workbook.sheet_names()[1]

    # 根据sheet索引或者名称获取sheet内容
    sheet2 = workbook.sheet_by_index(1)  # sheet索引从0开始
    # sheet2 = workbook.sheet_by_name('sample')

    # sheet的名称，行数，列数
    print sheet2.name, sheet2.nrows, sheet2.ncols

    # 获取整行和整列的值（数组）
    rows = sheet2.row_values(3)  # 获取第四行内容
    cols = sheet2.col_values(2)  # 获取第三列内容
    print rows
    print cols

    # 获取单元格内容
    print sheet2.cell(1, 0).value.encode('utf-8')
    print sheet2.cell_value(1, 0).encode('utf-8')
    print sheet2.row(1)[0].value.encode('utf-8')

    # 获取单元格内容的数据类型
    print sheet2.cell(1, 0).ctype


def ExcelStyle(name='Times New Roman', height=220, bold=False, frontColor=0, hasBorder=False, backGround=0,
               isCenter=True):
    style = xlwt.XFStyle()  # 初始化样式

    font = xlwt.Font()  # 为样式创建字体
    font.name = name  # 'Times New Roman'
    font.bold = bold
    font.colour_index = frontColor  # 2 红色 4 黑色
    font.height = height  # 字体大小 220 对应11pt 440 对应22pt
    style.font = font

    if backGround > 0:
        pattern = xlwt.Pattern()  # Create the Pattern
        pattern.pattern = xlwt.Pattern.SOLID_PATTERN  # May be: NO_PATTERN, SOLID_PATTERN, or 0x00 through 0x12
        pattern.pattern_fore_colour = 5  # 设置单元格背景颜色 0 = Black, 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow, 6 = Magenta,
        style.pattern = pattern  # Add Pattern to Style

    if hasBorder:
        borders = xlwt.Borders()
        borders.left = 1
        borders.right = 1
        borders.top = 1
        borders.bottom = 1
        borders.bottom_colour = 0x3A
        style.borders = borders  # Add borders  to Style

    if isCenter:
        alignment = xlwt.Alignment()
        alignment.horz = xlwt.Alignment.HORZ_CENTER  # 水平居中
        alignment.vert = xlwt.Alignment.VERT_CENTER  # 垂直居中
        style.alignment = alignment

    return style


def writeCell(sheet, row, col, value, style):
    sheet.write(row, col, value.decode('utf-8', 'ignore').style)


'''
filePath = 'xx.xls' 当前目录
'''


def createExcelWithSheetName(filePath, sheetName):
    wb = xlwt.Workbook()
    wb.add_sheet(sheetname=sheetName.decode('utf-8', 'ignore'), cell_overwrite_ok=True)
    sheet = wb.get_sheet(0)
    datas = [
        # 第一行内容
        {'isMerge': True, 'row_start': 0, 'row_end': 0, 'col_start': 0, 'col_end': 10, 'content': '员工工作日志',
         'style': ExcelStyle(height=440, bold=True)},
        # 第二行内容
        {'isMerge': False, 'row': 1, 'col': 0, 'content': '部门:', 'style': ExcelStyle(name=u'宋体', bold=True)},
        {'isMerge': False, 'row': 1, 'col': 1, 'content': '工程部', 'style': ExcelStyle(name=u'宋体', bold=True)},
        {'isMerge': False, 'row': 1, 'col': 3, 'content': '姓名:', 'style': ExcelStyle(name=u'宋体', bold=True)},
        {'isMerge': False, 'row': 1, 'col': 4, 'content': 'lzd', 'style': ExcelStyle(name=u'宋体', bold=True)},
        {'isMerge': False, 'row': 1, 'col': 5, 'content': '岗位:', 'style': ExcelStyle(name=u'宋体', bold=True)},
        {'isMerge': True, 'row_start': 1, 'row_end': 1, 'col_start': 6, 'col_end': 7, 'content': 'java开发工程师',
         'style': ExcelStyle(name=u'宋体', bold=True)},
        {'isMerge': False, 'row': 1, 'col': 8, 'content': '填表日期:', 'style': ExcelStyle(name=u'宋体', bold=True)},
        {'isMerge': False, 'row': 1, 'col': 9, 'content': time.strftime("%y/%m/%d"),
         'style': ExcelStyle(name=u'宋体', bold=True)},
        # 第三行内容
        {'isMerge': False, 'row': 2, 'col': 0, 'content': '序号',
         'style': ExcelStyle(name=u'宋体', bold=True, backGround=5, hasBorder=True)},
        {'isMerge': False, 'row': 2, 'col': 1, 'content': '工作时间',
         'style': ExcelStyle(name=u'宋体', bold=True, backGround=5, hasBorder=True)},
        {'isMerge': False, 'row': 2, 'col': 2, 'content': '工作类型',
         'style': ExcelStyle(name=u'宋体', bold=True, backGround=5, hasBorder=True)},

        {'isMerge': True, 'row_start': 2, 'row_end': 2, 'col_start': 3, 'col_end': 5, 'content': '具体内容',
         'style': ExcelStyle(name=u'宋体', bold=True)},
        {'isMerge': True, 'row_start': 2, 'row_end': 2, 'col_start': 6, 'col_end': 8, 'content': '输出成果',
         'style': ExcelStyle(name=u'宋体', bold=True)},

        {'isMerge': False, 'row': 2, 'col': 9, 'content': '耗时(分钟)',
         'style': ExcelStyle(name=u'宋体', bold=True, backGround=5, hasBorder=True)},
        {'isMerge': False, 'row': 2, 'col': 10, 'content': '备注',
         'style': ExcelStyle(name=u'宋体', bold=True, backGround=5, hasBorder=True)},
        {'isMerge': False, 'row': 2, 'col': 6, 'content': '哈哈',
         'style': ExcelStyle(name=u'宋体', bold=True, backGround=5, hasBorder=True)},
    ]

    for data in datas:
        if data.get('isMerge'):
            # x1,x2 ,y1,y2   第x1行到第x2行 y1列---y2列
            sheet.write_merge(data.get('row_start'), data.get('row_end'), data.get('col_start'), data.get('col_end'),
                              data.get('content').decode('utf-8', 'ignore'), data.get('style'))
        else:
            sheet.write(data.get('row'), data.get('col'), data.get('content').decode('utf-8', 'ignore'),
                        data.get('style'))
            pass

    wb.save(filePath)


def writeExcel(fileName):
    rootPath = os.path.dirname(os.path.dirname(os.getcwd()))  # 程序所在更目录：当前目录的上一层的上一层
    filePath = os.path.join(rootPath, fileName)  # 保存文件的全路径
    todaySheetName = time.strftime("%m月%d日")
    if not os.path.exists(filePath):
        createExcelWithSheetName(filePath, todaySheetName)

    rb = xlrd.open_workbook(fileName, formatting_info=True)  # 只能读不能写
    wb = xlutils.copy.copy(rb)  # 只能写不能读


if __name__ == '__main__':
    # read_excel()
    todaySheetName = time.strftime("%m月%d日")
    createExcelWithSheetName('create.xls', todaySheetName)
