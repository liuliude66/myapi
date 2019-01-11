#! python
# -*- coding:utf-8 -*-

from code.config.globalConfig import GlobalConfig
from code.special.testCase.betTest import BetTest
from code.special.testCase.loginTest import LoginTest

#  查看彩种布局
class AppUI(object):

    def __init__(self, lottery_name):
        try:
            #  账号 密码
            config = GlobalConfig()
            pre_dic = LoginTest().interfaceLoginCase(config.User_account, config.User_password)
            BetTest().interfaceBetCase(pre_dic, lottery_name)
        except Exception as ex:
            print(str(ex.args))

if __name__ == "__main__":
    AppUI(GlobalConfig.Lottery_bet)
