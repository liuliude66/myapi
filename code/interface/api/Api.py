#! /usr/bin/python
# -*- coding:utf-8 -*-

from __future__ import unicode_literals

import json, urllib.request

from code.interface.utils.Report import FileHelper
from code.config.globalConfig import GlobalConfig
from code.interface.utils.HtmlManager import *

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
    formData = 0  # 是否是formData参数
    index = 0  # 输入编号索引

    def __init__(self):
        self.header['content-type'] = 'application/json;charset:utf-8'
        self.header['user-agent'] = GlobalConfig['USER_AGENT']
        self.header['X-Requested-With'] = 'XMLHttpRequest'
        self.header['client-version'] = GlobalConfig['Client_version']
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
                    response = '请求异常:' + str(urllib.request.urlopen(self.url).getcode()) + str(tuple(e.args))
                except Exception as e:
                    response = '服务器url请求错误'
        print('编号:%s' % (self.index + 1))
        print(response)
        # 保存测试结果
        try:
            if isinstance(response, str):
                result = 'error'
                GlobalConfig['ERROR_COUNT'] = GlobalConfig['ERROR_COUNT'] + 1
            elif self.expect == response['code']:
                result = 'pass'
                GlobalConfig['SUCCESS_COUNT'] = GlobalConfig['SUCCESS_COUNT'] + 1
            else:
                if self.expect == '':
                    result = 'exception'
                    GlobalConfig['EXCEPTION_COUNT'] = GlobalConfig['EXCEPTION_COUNT'] + 1
                else:
                    result = 'fail'
                    GlobalConfig['FAILURE_COUNT'] = GlobalConfig['FAILURE_COUNT'] + 1
                    temp = dict()
                    temp['code'] = response['code']
                    if 'msg' in response.keys():
                        temp['msg'] = response['msg']
                    else:
                        temp['msg'] = '后台最后返回下msg'
                    response = temp
        except Exception as ex:
            result = 'error'
            GlobalConfig['ERROR_COUNT'] = GlobalConfig['ERROR_COUNT'] + 1
            print(ex.args)
        html = generate_html_file(self.index + 1, self.case_name, self.url, self.parameter, self.expect, json.dumps(response, ensure_ascii=False), result, self.requestTime)
        helper = FileHelper()
        helper.write(html)

    def action(self):
        pass
