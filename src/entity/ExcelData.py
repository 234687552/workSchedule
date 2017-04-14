# -*- coding: utf-8 -*-

class ExcelData(object):
    def __init__(self, workType, content, result, remarks):
        self._workType = workType #工作类型 固定工作/非固定工作
        self._content = content #工作内容
        self._result = result #输出结果
        self._remarks = remarks #备注

    @property
    def workType(self):
        return self._workType

    @workType.setter
    def workType(self, value):
        self._workType = value

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value

    @property
    def remarks(self):
        return self._remarks

    @remarks.setter
    def remarks(self, value):
        self._remarks = value
