#! /usr/bin/python
# -*- coding:utf-8 -*-

from com.forum.special.tool.transTool import TransLogin
from com.forum.special.tool.assertTool import assertCode
from com.forum.special.service.loginHttpTool import LoginHttpTool
from com.forum.special.tool.testConfig import PostParamList, PostParam, TestConfig
from com.forum.special.testCase.publicHandle import PublicHandle

# 登录模块测试
class LoginTest(PublicHandle):
    def specialRegisteCase(self): # 注册专项测试
        success0, result0 = LoginHttpTool.postRegisterOption()
        if success0 == 1:
            return result0, []
        else:
            configDic = TestConfig.getRegisteData()
            listItem = TransLogin().TransSpecial(configDic)
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
            return {'items': htmlList, 'options' : result0}

    def specialLoginCase(self): # 登录专项测试
        configDic = TestConfig.getLoginData()
        listItem = TransLogin().TransSpecial(configDic)
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
            if success2 == 1:
                print('error')
            else:
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
            if success2 == 1:
                print('error')
            else:
                return htmlList