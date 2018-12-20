#! /usr/bin/python
# -*- coding:utf-8 -*-

from com.forum.special.htmls.createHtml import *
from com.forum.tool.testConfig import *

DicItems = 'items'

# 接口显示
def handleInterfaceData(starttime, endtime, resultDic, configDic):
    titles = '%s模块接口自动化测试报告' % configDic[OutputName]
    headerItems = configDic[ExcelItem] + configDic[ExtraResult]
    showIds = configDic[ParamList]
    items = resultDic
    fileName = configDic[OutputName]
    failue = 0
    success = 0
    for i in range(len(items)):
        if items[i]['isPass'] == 0:
            success += 1
        else:
            failue += 1
    tatistics = dataOutline('', starttime, endtime, str(success), str(failue))
    tableHeader = createTableHeader(headerItems)
    if type(items) == list:
        relus = ''
        for i in range(len(items)):
            item = items[i]
            item['listItem']['id'] = i
            relus += (renderItem(item, showIds))
        text = htmlTitle(titles) + \
               testRegion(fileName) + \
               tatistics + \
               tableHeader + \
               relus + \
               htmlFooter
        outputFile(text, fileName)
    else:
        text = htmlTitle(titles) + \
               testRegion(fileName) + \
               tableHeader + \
               htmlFooter
        outputFile(text, fileName)
    return