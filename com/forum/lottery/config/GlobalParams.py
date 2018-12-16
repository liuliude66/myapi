#! /usr/bin/python
# -*- coding:utf-8 -*-

GlobalConfig = {
    'MAX_RETRY': 3,  # 请求错误最大重试次数
    'REQUEST_TIMEOUT': 15,  # 网络超时请求时间
    'DOMAIN': 'http://5550987.com',  # 网络请求域名
    'Client_version': "5.2.3", #当前版本号
    'SESSION_ID': '',  # sessionid 请求头中
    'USER_ID': '',  # userid 可能用做参数
    'SUCCESS_COUNT': 0,  # 成功的个数
    'FAILURE_COUNT': 0,  # 失败的个数
    'ERROR_COUNT': 0,  # 异常的个数
    'EXCEPTION_COUNT': 0,  # 未知错误的个数
    'REPORT_PATH': 'D:/PycharmProjects/APITest/files/report/',  # 测试报告文档
    'TEST_CASE_PATH': 'D:/PycharmProjects/APITest/files/xlsx/case123.xlsx'  # 测试用例路径
}
