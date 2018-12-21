#! /usr/bin/python
# -*- coding:utf-8 -*-

from rootPath import getRootPath

GlobalConfig = {
    'MAX_RETRY': 3,  # 请求错误最大重试次数
    'REQUEST_TIMEOUT': 15,  # 网络超时请求时间
    'DOMAIN': 'http://msg2.0234.co',  # 网络请求域名
    'Client_version': "5.2.3",  # 当前版本号
    'username': "1002",   # 投注测试账号
    'password': "123456",   # 投注测试密码
    'SUCCESS_COUNT': 0,  # 成功的个数
    'FAILURE_COUNT': 0,  # 失败的个数
    'ERROR_COUNT': 0,  # 异常的个数
    'EXCEPTION_COUNT': 0,  # 未知错误的个数
    'REPORT_PATH': getRootPath() + '/files/report/',  # 测试报告文档路径
}