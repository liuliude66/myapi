#! /usr/bin/python
# -*- coding:utf-8 -*-

from rootPath import getRootPath

class GlobalConfig(object):
    Domain = 'http://msg2.0234.co'  # 网络请求域名
    Client_version = '5.2.3'        # 当前版本号
    Max_retry = 1                   # 请求错误最大重试次数
    Request_timeout = 15            # 网络超时请求时间
    User_agent = 'SSCBeta'          # 请求头代理
    X_requested_with = 'XMLHttpRequest'  # 请求头参数
    Success_count = 0               # 成功的个数
    Failure_count = 0               # 失败的个数
    Error_count = 0                 # 异常的个数
    Exception_count = 0             # 未知错误的个数
    Report_path = getRootPath() + '/files/report/'  # 测试报告文档路径

    # 测试数据配置
    User_account = '1002'           # 投注测试账号
    User_password = '123456'        # 投注测试密码
    Lottery_layout = '江苏快3'       # 布局——彩种名称
    Lottery_bet = '安徽快3'          # 投注——彩种名称
