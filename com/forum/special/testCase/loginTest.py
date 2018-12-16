#! /usr/bin/python
# -*- coding:utf-8 -*-

import datetime

from com.forum.special.tool.transTool import TransTool
from com.forum.special.tool.assertTool import assertCode
from com.forum.special.service.loginHttpTool import LoginHttpTool
from com.forum.special.testCase.publicHandle import PublicHandle
from com.forum.special.htmls.loginModuleHtml import *

# 登录模块测试
class LoginTest(PublicHandle):
    def specialRegisteCase(self): # 注册专项测试
        starttime = datetime.datetime.now()
        success0, result0 = LoginHttpTool.postRegisterOption()
        htmlList = []
        if success0 == 1:
            print('error')
        else:
            configDic = TestConfig.getRegisteData()
            listItem = TransTool().TransSpecial(configDic)
            for i in range(len(listItem)):
                success, result = LoginHttpTool.postGetSessionid()
                if success == 1:
                    sessionDict = dict()
                    sessionDict['listItem'] = listItem[i]
                    sessionDict['result'] = self.showResultSuccessDic(result)
                    sessionDict['isPass'] = 1
                    htmlList.append(sessionDict)
                    continue
                else:
                    params = dict()
                    item = listItem[i]
                    itemDict = dict()
                    itemDict['listItem'] = item
                    postParamList = configDic[PostParamList]
                    for i in range(len(postParamList)):
                        if item[postParamList[i]] != '':
                            params[postParamList[i]] = item[postParamList[i]]
                    success1, result1 = LoginHttpTool.postRegister(params)
                    itemDict['result'] = self.showResultSuccessDic(result1)
                    if success1 == 1:
                        itemDict['isPass'] = 1
                        htmlList.append(itemDict)
                        continue
                    else:
                        assertResult = assertCode('0', result1['code'])
                        if assertResult['code'] == 0:
                            itemDict['isPass'] = 0
                            htmlList.append(itemDict)
                            continue
                        else:
                            itemDict['isPass'] = 1
                            htmlList.append(itemDict)
                            continue
        endtime = datetime.datetime.now()
        handleRegisterHtmlData(starttime, endtime, {'items': htmlList, 'options' : result0})
        return {'items': htmlList, 'options' : result0}

    def specialLoginCase(self): # 登录专项测试
        starttime = datetime.datetime.now()
        configDic = TestConfig.getLoginData()
        listItem = TransTool().TransSpecial(configDic)
        htmlList = []
        for i in range(len(listItem)):
            success, result = LoginHttpTool.postGetSessionid()
            if success == 1:
                sessionDict = dict()
                sessionDict['listItem'] = listItem[i]
                sessionDict['result'] = self.showResultSuccessDic(result)
                sessionDict['isPass'] = 1
                htmlList.append(sessionDict)
                continue
            else:
                params = dict()
                item = listItem[i]
                itemDict = dict()
                itemDict['listItem'] = item
                postParamList = configDic[PostParamList]
                for i in range(len(postParamList)):
                    if item[postParamList[i]] != '':
                        params[postParamList[i]] = item[postParamList[i]]
                success1, result1 = LoginHttpTool.postLogin(params)
                itemDict['result'] = self.showResultSuccessDic(result1)
                if success1 == 1:
                    itemDict['isPass'] = 1
                    htmlList.append(itemDict)
                    continue
                else:
                    assertResult = assertCode('0', result1['code'])
                    if assertResult['code'] == 0:
                        itemDict['isPass'] = 0
                        htmlList.append(itemDict)
                        continue
                    else:
                        itemDict['isPass'] = 1
                        htmlList.append(itemDict)
                        continue
        endtime = datetime.datetime.now()
        handleLoginHtmlData(starttime, endtime, {'items': htmlList})
        return {'items': htmlList}

    def interfaceRegisteCase(self):
        configDic = TestConfig.getRegisteInterfaceData()
        htmlList = []
        success1, result1 = LoginHttpTool.postGetSessionid()
        htmlList.append(self.showInterfaceDic(result1, '获取sessionId'))
        if success1 == 1:
            print('error')
        else:
            success2, result2 = LoginHttpTool.postRegister(configDic[PostParam])
            htmlList.append(self.showInterfaceDic(result2, '注册'))
        return htmlList

    def interfaceLoginCase(self):
        configDic = TestConfig.getLoginInterfaceData()
        htmlList = []
        success1, result1 = LoginHttpTool.postGetSessionid()
        htmlList.append(self.showInterfaceDic(result1, '获取sessionId'))
        if success1 == 1:
            print('error')
        else:
            success2, result2 = LoginHttpTool.postLogin(configDic[PostParam])
            htmlList.append(self.showInterfaceDic(result2, '登录'))
        return htmlList