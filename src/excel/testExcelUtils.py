# -*- coding: utf-8 -*-
import xlrd
import xlwt
import xlutils.copy


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


def copy_sheet(fileName, source_sheet_index, new_sheet_name, outputName):
    readBook = xlrd.open_workbook(fileName, formatting_info=True)  # formatting_info 带格式导入

    outwb = xlutils.copy.copy(readBook)  # 建立一个副本来用xlwt来写

    sourceSheet = outwb.get_sheet(source_sheet_index)

    outwb._Workbook__worksheets.append(sourceSheet)  # copy sheet
    # outwb._Workbook__worksheets[2]._Worksheet__name = new_sheet_name
    outwb.save(outputName)
    # outwb.get_sheet(2).set_name(new_sheet_name)

    #上面只是复制了sheet 但是修改不了复制出来的sheet的名字 下面是改名字
    readBook2 = xlrd.open_workbook(outputName, formatting_info=True)  # formatting_info 带格式导入
    outwb2 = xlutils.copy.copy(readBook2)
    outwb2._Workbook__worksheets[-1]._Worksheet__name = new_sheet_name
    outwb2.save(outputName)



copy_sheet('15.xls', 0, 'hhe', 'test.xls')
