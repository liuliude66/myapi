#! /usr/bin/python
# -*- coding:utf-8 -*-

import xlrd, os

from xlrd import xldate_as_tuple
from datetime import datetime
from com.forum.special.tool.testConfig import ExcelName, ParamList

basePath = os.getcwd() + '/files/xlsx/'

class TransTool:
    def TransSpecial(self, configDic):
        try:
            file = xlrd.open_workbook(basePath + '%s.xlsx' % configDic[ExcelName])
            me = file.sheets()[0]
            nrows = me.nrows
            result = []
            itemList = configDic[ParamList]
            for i in range(1, nrows):
                item = dict()
                for j in range(len(itemList)):
                    ctype = me.cell(i, j).ctype
                    cell = me.cell_value(i, j)
                    if ctype == 2 and cell % 1 == 0:
                        cell = int(cell)
                    elif ctype == 3:
                        date = datetime(*xldate_as_tuple(cell, 0))
                        cell = date.strftime('%Y/%d/%m %H:%M:%S')
                    elif ctype == 4:
                        cell = True if cell == 1 else False
                    item[itemList[j]] = cell
                result.append(item)
            return result
        except Exception as e:
            print('打开测试用例失败，原因是:%s' % e)
            return