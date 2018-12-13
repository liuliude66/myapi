#! /usr/bin/python
# -*- coding:utf-8 -*-
from __future__ import unicode_literals
import xlrd
from com.forum.lottery.config.GlobalParams import GlobalConfig


#  Excel 读取器
def read_excel():
    result = []
    try:
        file_path = GlobalConfig['TEST_CASE_PATH']
        data = xlrd.open_workbook(file_path)
        table = data.sheets()[0]
        rows = table.nrows
        for i in range(1, rows):
            item = dict()
            item['case_name'] = table.cell(i, 1).value
            item['parameter'] = table.cell(i, 3).value
            # if item['parameter']:
            #     item['parameter'] = item['parameter'].encode('UTF-8')
            item['request_url'] = table.cell(i, 4).value
            item['request_method'] = table.cell(i, 5).value
            item['request_expect'] = table.cell(i, 6).value
            item['test_switch'] = table.cell(i, 7).value
            result.append(item)
        # print(result)
    except Exception as ex:
        print(ex.args)
    return result
