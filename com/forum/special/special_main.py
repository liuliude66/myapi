# -*- coding: utf-8 -*-
# @Author  : leizi

import datetime

from com.forum.special.testCase.loginTest import LoginTest
from com.forum.special.htmls.loginModuleHtml import handleLoginHtmlData

'''执行测试的主要文件'''
def start_interface_html_http():
    starttime = datetime.datetime.now()
    # 注册专项
    # resultDic = LoginTest().specialRegisteCase()
    # endtime = datetime.datetime.now()
    # handleRegisterHtmlData(starttime, endtime, resultDic)

    #登录专项
    resultDic = LoginTest().specialLoginCase()
    endtime = datetime.datetime.now()
    handleLoginHtmlData(starttime, endtime, resultDic)

    # resultDic = LoginTest().interfaceLoginCase()
    # endtime = datetime.datetime.now()
    # handleInterfaceData(starttime, endtime, resultDic)

    # 投注测试 (注册）
    # preDic = LoginTest().interfaceRegisteCase()
    # resultDic = BetTest().interfaceBetCase()
    # endtime = datetime.datetime.now()
    # print(preDic + resultDic)
    # handleInterfaceData(starttime, endtime, preDic + resultDic, TestConfig().getBetInterfaceData())

    # 所有彩种布局请求
    # resultDic = BetTest().interfaceLotteryLayoutCase()
    # endtime = datetime.datetime.now()
    # handleInterfaceData(starttime, endtime, resultDic, TestConfig().getNormalInterfaceData('彩种布局'))

    # 投注测试 (登录）
    # preDic = LoginTest().interfaceLoginCase()
    # resultDic = BetTest().interfaceBetCase()
    # endtime = datetime.datetime.now()
    # handleInterfaceData(starttime, endtime, preDic + resultDic, TestConfig().getBetInterfaceData())

if __name__ == '__main__':
    start_interface_html_http()