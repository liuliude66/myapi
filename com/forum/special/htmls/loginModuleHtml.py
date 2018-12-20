#! /usr/bin/python
# -*- coding:utf-8 -*-

DicItems = 'items'

from com.forum.special.htmls.createHtml import *
from com.forum.special.service.urlService import LoginModule
from com.forum.tool.testConfig import *

# 注册专项
def handleRegisterHtmlData(starttime, endtime, resultDic):
    url = LoginModule.urlRegister
    configDic = TestConfig().getRegisteData()
    titles = '%s模块接口自动化测试报告' % configDic[OutputName]
    headerItems = configDic[ExcelItem] + configDic[ExtraResult]
    showIds = configDic[ParamList]
    items = resultDic[DicItems]
    optionResult = resultDic['options']
    fileName = configDic[OutputName]
    failue = 0
    success = 0
    for i in range(len(items)):
        if items[i]['isPass'] == 0:
            success += 1
        else:
            failue += 1
    tatistics = dataOutline(url, starttime, endtime, str(success), str(failue))
    tableHeader = createTableHeader(headerItems)
    if type(items) == list:
        relus = ''
        for i in range(len(items)):
            relus += (renderItem(items[i], showIds))
        text = htmlTitle(titles) + \
               testRegion(fileName) + \
               tatistics + \
               createRegisterOptions(optionResult) + \
               tableHeader + \
               relus + \
               htmlFooter
        outputFile(text, fileName)
    else:
        text = htmlTitle(titles) + \
               testRegion(fileName) + \
               tatistics + \
               createRegisterOptions(optionResult) + \
               tableHeader + \
               htmlFooter
        outputFile(text, fileName)
    return

# 登录专项
def handleLoginHtmlData(starttime, endtime, resultDic):
    url = LoginModule.urlLogin
    configDic = TestConfig().getLoginData()
    titles = '%s模块接口自动化测试报告'%configDic[OutputName]
    headerItems = configDic[ExcelItem] + configDic[ExtraResult]
    showIds = configDic[ParamList]
    items = resultDic[DicItems]
    fileName = configDic[OutputName]
    failue = 0
    success = 0
    for i in range(len(items)):
        if items[i]['isPass'] == 0:
            success += 1
        else:
            failue += 1
    tatistics = dataOutline(url, starttime, endtime, str(success), str(failue))
    tableHeader = createTableHeader(headerItems)
    if type(items) == list:
        relus = ''
        for i in range(len(items)):
            relus += (renderItem(items[i], showIds))
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
               tatistics + \
               tableHeader + \
               htmlFooter
        outputFile(text, fileName)
    return

def createRegisterOptions(option):
    if option['code'] != 0:
        return '<p>注册选项配置获取失败: code:%s, msg:%s</p>'%(option['code'], option['msg'])
    else:
        text =  '''<div style="margin-top: 20px;width: 300px;margin-left: 50px;">
            <div style="padding-left:15px;"><strong>注册可选项:</strong></div>
            <div class="panel-body">
                <div class="table-responsive" style="border:1px solid #ddd;">
                    <table class="table table-striped">
                        <thead><tr><th style="width:100px">属性名称</th><th style="width:100px">显示</th><th style="width:100px">必填</th></tr></thead>
                        <tbody>'''
        for i in range(len(option['data'])):
            item = option['data'][i]
            showStr = '显示'
            if item['show'] == 0:
                showStr = '隐藏'
            requireStr = '是'
            if item['required'] == 0:
                requireStr = '否'
            text += '<tr id="1"><td>%s</td><td><span>%s</span></td><td><span>%s</span></td></tr>'%(item['name'], showStr, requireStr)
        text += '''</tbody>
                </table>
                </div>
                </div>
            </div>'''
        return text

