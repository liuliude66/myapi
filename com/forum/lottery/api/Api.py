#! /usr/bin/python
# -*- coding:utf-8 -*-
import json
import simplejson
from com.forum.lottery.utils.Report import FileHelper
from com.forum.lottery.utils.HtmlManager import *

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
                message = str(tuple(e.args))
                response = json.loads(message)
        print(response)
        # 保存测试结果
        th_header = 'hello test result'
        try:
            expect_json = eval(self.expect)

            if expect_json['code'] == response['code']:
                result = 'pass'
                GlobalConfig['SUCCESS_COUNT'] = GlobalConfig['SUCCESS_COUNT'] + 1
            else:
                result = 'fail'
                GlobalConfig['FAILURE_COUNT'] = GlobalConfig['FAILURE_COUNT'] + 1
        except Exception as ex:
            result = 'error'
            GlobalConfig['ERROR_COUNT'] = GlobalConfig['ERROR_COUNT'] + 1
            print(ex.args)
        html = generate_html_file(th_header, self.case_name, self.url, json.dumps(self.parameter), self.expect, json.dumps(response), result)
        helper = FileHelper()
        helper.write(html)

    def action(self):
        pass
