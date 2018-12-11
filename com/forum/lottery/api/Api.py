#! /usr/bin/python
# -*- coding:utf-8 -*-
import time
from com.forum.lottery.utils.Report import FileHelper


# 父类验证
class Api(object):
    domain = 'http://msg2.0234.co/'
    url = ''
    timeout = 10
    header = {}
    parameter = {}

    def __init__(self):
        self.header['content-type'] = 'application/json;charset:utf-8'
        self.header['user-agent'] = 'SSC/5.2.3(Android 7.0.0; version)'
        self.header['X-Requested-With'] = 'XMLHttpRequest'
        self.header['client-version'] = '5.2.3'
        self.header['sessionid'] = ''

    def run(self):
        try:
            start = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            self.action()
            end = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            content = "以下该接口成功执行，并记录下起止时间：\n" + start + "\n" + self.url + "\n" + end + "\n"
            helper = FileHelper()
            helper.write(content)
        except Exception as e:
            helper = FileHelper()
            helper.write(e.args)

    def action(self):
        pass
