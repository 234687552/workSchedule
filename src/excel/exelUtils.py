# -*- coding: utf-8 -*-
import os

import time
import xlrd
import xlwt
from datetime import date

from src.base.ReturnInfo import ReturnInfo

'''
# 读取Excel数据
#
# 参数:
#         file_name    : xls文件，含路径
#         col_list    : 读取数据后对应的列字段，如: ['id' , 'name' , 'value']
# 返回: List
'''


def readExcel(file_name, col_list):
    # 判断文件是否存在，以及是否以xls后缀
    if not os.path.isfile(file_name) or os.path.basename(file_name).split('.')[1] != 'xls':
        return ReturnInfo(-1, 'file is not valid')

    try:
        # 打开Excel文件
        curBook = xlrd.open_workbook(file_name)

        # 获取Sheet表, Sheet索引起始为0.
        sheet1 = curBook.sheet_by_index(0)

        # 或者，通过Sheet名称获取相应的Sheet
        # sheet1_name = curBook.sheet_names()[0]
        # sheet1 = curBook.sheet_by_name(sheet1_name)

        # 获取Sheet行数
        rowNum = sheet1.nrows
        # 获取Sheet列数
        # colNum = sheet1.ncols
        # 此处，以实际接受的字段为准
        colNum = len(col_list)

        # 用于接收数据
        dataList = []

        # 默认从第二行开始读取，第一行为列标题
        '''
            # 读取单元格的值 : A2
            sheet1.cell(1,0).value
            sheet1.cell_value(rowx=1, colx=0)
            sheet1.row(1)[0].value.encode('utf-8')

            # 单元格的类型
            # ctype : 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
            sheet1.cell(1,0).ctype
        '''

        # 循环读取行数据
        for i in range(1, rowNum):
            curRow = {}
            # 读取行内各列
            for j in range(colNum):
                #
                if sheet1.cell(i, j).ctype == 3:
                    # 如果单元格的数据为日期类型，读取后得到是浮点数；此处进行格式化处理
                    date_value = xlrd.xldate_as_tuple(sheet1.cell_value(i, j), curBook.datemode)
                    curRow[col_list[j]] = date(*date_value[:3]).strftime('%Y-%m-%d')
                else:
                    curRow[col_list[j]] = sheet1.cell(i, j).value
            # 行数据保存到list
            dataList.append(curRow)

    # 异常处理
    except Exception as e:
        print('Error:', e)
        return ReturnInfo(-1, 'file read failed')

    return ReturnInfo(0, dataList)


'''
# 写入数据到Excel
#
# 参数:
#         dataList    : 数据列表，如[{'id':1,'name':'ice cream','value':66},...]
#         file_title    : 文件标题
#         col_list    : 列字段及列标题，如: [['id','序号'],['name','名称'],...]
#         isSave        : 是否保存到指定路径；否表示输出到浏览器
#         savePath    : 保存路径
# 返回: Mixed
'''


def writeExcel(dataList, file_title, col_list, isSave=False, savePath=''):
    # 添加后缀，指定文件的名称
    fileName = file_title + time.strftime("_%Y%m%d%H%M%S", time.localtime()) + '.xls'

    try:
        # 创建workbook对象
        curBook = xlwt.Workbook()
        # 设定编码
        curBook.encoding = 'gbk'
        # 添加Sheet表；其中cell_overwrite_ok，表示是否可以覆盖单元格
        sheet1 = curBook.add_sheet(u'sheet1', cell_overwrite_ok=True)

        # 行数
        rowNum = len(dataList)
        # 列数
        colNum = len(col_list)

        # 第一行，合并单元格，设定文件标题
        # write_merge(x, x + h, y, y + w, string, style)，x表示行，y表示列，h表示跨行个数，w表示跨列个数
        sheet1.write_merge(0, 0, 0, colNum - 1, file_title, set_style('华文中宋', 320))

        # 第二行，设定列标题
        colTitleStyle = set_style('华文宋体', 240)
        for k in range(0, colNum):
            sheet1.write(1, k, col_list[k][1], colTitleStyle)

        # 第三行起，开始写入数据
        for i in range(0, rowNum):
            for j in range(0, colNum):
                sheet1.write(i + 2, j, dataList[i][col_list[j][0]])

        if isSave:
            # 如保存xls到路径
            full_filename = os.path.join(savePath, fileName)
            # 执行保存
            curBook.save(full_filename)
            return ReturnInfo(0, "succeed保存")
        else:
            # 否则输出到浏览器
            return ReturnInfo(-1, "保存失败")
    # 异常处理
    except Exception as e:
        print('Error:', e)
        return ReturnInfo(-1, 'data export failed')


'''
# 设定样式
#
# 参数:
#         font_name    : 字体
#         font_height    : 字体大小，注：20 = 1pt
#         font_bold    : 字体是否加粗
#         border        : 是否设置边框
# 返回: Style
'''


def set_style(font_name='Times New Roman', font_height=220, font_bold=False, border=False):
    # 初始化Style
    style = xlwt.XFStyle()

    # 设定字体样式
    font = xlwt.Font()
    font.name = font_name
    font.color_index = 4
    font.height = font_height  #
    font.bold = font_bold
    style.font = font

    # 设定边框属性
    if border:
        borders = xlwt.Borders()
        borders.left = 1
        borders.right = 1
        borders.top = 1
        borders.bottom = 1
        style.borders = borders

    # 居中对齐，'general': 0 , 'left': 1 , 'centre': 2 , 'right': 3, ...
    style.alignment.horz = 2
    # 水平对齐，HORZ_GENERAL, HORZ_LEFT, HORZ_CENTER, HORZ_RIGHT, ...
    # 竖直对齐，VERT_TOP, VERT_CENTER, VERT_BOTTOM, ...
    # style.alignment.horz = xlwt.Alignment.HORZ_CENTER
    # style.alignment.vert = xlwt.Alignment.VERT_CENTER

    # 设置背景颜色
    # pattern = xlwt.Pattern()
    # pattern.pattern = xlwt.Pattern.SOLID_PATTERN
    # pattern.pattern_fore_colour = 5
    # style.pattern = pattern

    # 其他，可参见xlwt源码

    # 或者使用easyxf
    # style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on' , num_format_str='#,##0.00')

    # 返回样式
    return style
