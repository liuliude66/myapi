#! /usr/bin/python
# -*- coding:utf-8 -*-

from __future__ import unicode_literals

import json, urllib.request

from com.forum.lottery.utils.HtmlManager import *
from com.forum.lottery.utils.Report import FileHelper

# API父类
class Api(object):
    domain = GlobalConfig['DOMAIN']
    url = ''
    timeout = GlobalConfig['REQUEST_TIMEOUT']
    header = {}
    parameter = {}
    api_response = {}
    expect = ''
    case_name = ''
    requestTime = 0
    formData = 0

    def __init__(self):
        self.header['content-type'] = 'application/json;charset:utf-8'
        self.header['user-agent'] = 'SSC/5.2.3(Android 7.0.0; version)'
        self.header['X-Requested-With'] = 'XMLHttpRequest'
        self.header['client-version'] = '5.2.3'
        self.header['sessionid'] = ''

    def run(self):
        index = 0
        response = {}
        while index < GlobalConfig['MAX_RETRY']:
            index = index + 1
            try:
                response = self.action()
                break
            except Exception as e:
                print("重试次数:" + str(index))
                try:
                    response = '请求异常:' + str(urllib.request.urlopen(GlobalConfig['DOMAIN'] + self.url).getcode()) + str(tuple(e.args))
                except Exception as e:
                    response = '服务器url请求错误'
        print(response)
        # 保存测试结果
        th_header = 'hello test result'
        try:
            if isinstance(response, str):
                result = 'exception'
                GlobalConfig['EXCEPTION_COUNT'] = GlobalConfig['EXCEPTION_COUNT'] + 1
            elif self.expect == response['code']:
                result = 'pass'
                GlobalConfig['SUCCESS_COUNT'] = GlobalConfig['SUCCESS_COUNT'] + 1
            else:
                result = 'fail'
                GlobalConfig['FAILURE_COUNT'] = GlobalConfig['FAILURE_COUNT'] + 1
                temp = dict()
                temp['code'] = response['code']
                temp['msg'] = response['msg']
                response = temp
        except Exception as ex:
            result = 'error'
            GlobalConfig['ERROR_COUNT'] = GlobalConfig['ERROR_COUNT'] + 1
            print(ex.args)
        html = generate_html_file(th_header, self.case_name, self.url, json.dumps(self.parameter, ensure_ascii=False), self.expect,
                                  json.dumps(response, ensure_ascii=False), result, self.requestTime)
        helper = FileHelper()
        helper.write(html)

    def action(self):
        pass
