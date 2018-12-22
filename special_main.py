#! python
# -*- coding:utf-8 -*-

from com.special.testCase.loginTest import LoginTest
from com.special.testCase.betTest import BetTest

'''执行测试的主要文件'''
def start_interface_html_http():
    # 注册专项
    LoginTest().specialRegisteCase()

    # 登录专项
    LoginTest().specialLoginCase()

    # 所有彩种布局请求
    BetTest().interfaceLotteryLayoutCase('三分PK10')

    # 投注测试 (登录)
    preDic = LoginTest().interfaceLoginCase('lilei8', '888888')
    BetTest().interfaceBetCase(preDic, '三分PK10')

if __name__ == '__main__':
    start_interface_html_http()