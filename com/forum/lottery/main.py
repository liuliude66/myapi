#! python
# -*- coding:utf-8 -*-

from com.forum.lottery.api.LoginApi import LoginApi
from com.forum.lottery.api.CountdownApi import CountdownApi
from com.forum.lottery.api.LotteryApi import LotteryApi
from com.forum.lottery.api.BetRecordApi import BetRecordApi
from com.forum.lottery.api.RechargeRecordApi import RechargeRecordApi
from com.forum.lottery.api.RechargePayWayApi import RechargePayWayApi
from com.forum.lottery.api.BankInfoApi import BankInfoApi

if __name__ == '__main__':

    print("------->  start  <-------")
    # 登录接口
    username = '1002'
    password = '123456'
    print("------->  登录接口  <-------")
    LoginApi(username, password).run()

    # 倒计时接口
    print("------->  倒计时接口  <-------")
    CountdownApi().run()

    # 开奖接口
    print("------->  开奖接口  <-------")
    LotteryApi().run()

    #投注记录查询接口
    print("------->  投注记录查询接口  <-------")
    BetRecordApi().run()

    #充值记录查询接口
    print("------->  充值记录查询接口  <-------")
    RechargeRecordApi().run()

    #充值方式接口
    print("------->  充值方式接口  <-------")
    RechargePayWayApi().run()

    #银联卡绑定信息接口
    print("------->  银联卡绑定信息接口  <-------")
    BankInfoApi().run()
    print("------->  over  <-------")
