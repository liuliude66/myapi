#! /usr/bin/python
# -*- coding:utf-8 -*-

# 登录模块
class LoginModule():
    # 请求sessionId
    urlSessionId = "/passport/distribute_sessionid.do"
    # 获取注册选项
    urlRegisterOptions = "/agent/generalize/register_options.do"
    # 注册
    urlRegister = "/passport/register.do"
    # 登录
    urlLogin = "/passport/login.do"
    # 退出/注销
    urlLogout = "/passport/logout.do"

# 投注模块
class BetModule():
    # 彩种列表
    urlBetAllLottery = '/front/lottery/init.do'
    # 投注模块
    urlBetPlayGroupItems = '/front/lottery/lottery_group.do'
    # 请求布局参数
    urlBetGetLayoutItem = '/front/lottery/lottery_play_way.do'
    # 投注
    urlBetBetting = '/front/bet/betting.do'
    # 自动续到下一期
    urlBetBettingNextPeriod = '/front/bet/rebetting.do'