#! /usr/bin/python
# -*- coding:utf-8 -*-

from com.forum.lottery.common.Singleton import Singleton

class PublicHandle():
    def showResultSuccessDic(self, result): # 成功返回的显示
        showDic = dict()
        showDic['code'] = result['code']
        if 'msg' in result.keys():
            showDic['msg'] = result['msg']
        else:
            showDic['msg'] = '没有返回msg,让后台加'
        showDic['requestTime'] = result['requestTime']
        showDic['url'] = result['url']
        return showDic
    def showInterfaceDic(self, result, urlName):
        interfaceDic = dict()
        resultDic = dict()
        if result['code'] == 0:
            resultDic['code'] = result['code']
            if 'msg' in result.keys():
                resultDic['msg'] = result['msg']
            else:
                resultDic['msg'] = '没有返回msg,让后台加'
            resultDic['requestTime'] = result['requestTime']
            resultDic['url'] = result['url']
        else:
            resultDic = result
        interfaceDic['result'] = resultDic
        # 额外的参数
        listItemDic = dict()
        listItemDic['name'] = urlName
        listItemDic['url'] = result['url']
        listItemDic['id'] = 0
        if 'params' in result.keys():
            listItemDic['params'] = result['params']
        else:
            listItemDic['params'] = ''
        listItemDic['isLogin'] = '是'
        if Singleton().getSessionId() == '':
            listItemDic['isLogin'] = '否'
        interfaceDic['listItem'] = listItemDic

        if result['code'] == 0:
            interfaceDic['isPass'] = 0
        else:
            interfaceDic['isPass'] = 1
        return interfaceDic