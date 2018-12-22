#! python
# -*- coding:utf-8 -*-

from code.config.globalConfig import GlobalConfig
from code.special.testCase.betTest import BetTest

#  查看彩种布局
class AppUI(object):

    def __init__(self, lottery_name):
        self.lottery_layout_action(lottery_name)

    def lottery_layout_action(self, lottery_name):
        try:
            print(lottery_name)
            BetTest().interfaceLotteryLayoutCase(lottery_name)
        except Exception as ex:
            print(str(ex.args))

if __name__ == "__main__":
    AppUI(GlobalConfig['Lottery_layout'])
