#! python
# -*- coding:utf-8 -*-

from com.forum.lottery.api.LoginApi import LoginApi
from com.forum.lottery.api.CountdownApi import CountdownApi
from com.forum.lottery.api.LotteryApi import LotteryApi
from com.forum.lottery.api.BetRecordApi import BetRecordApi

if __name__ == '__main__':

    print("------->  start  <-------")
    # 登录接口
    username = '1002'
    password = '123456'
    LoginApi(username, password).run()

    # 倒计时接口
    CountdownApi().run()

    # 开奖接口
    LotteryApi().run()

    #投注记录查询接口
    BetRecordApi().run()
    print("------->  over  <-------")
