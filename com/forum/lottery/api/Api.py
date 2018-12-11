#! /usr/bin/python
# -*- coding:utf-8 -*-


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
        print('------> start test action should get current time<-----')
        try:
            self.action()
        except Exception as e:
            print(e.args)
        print('------> finish test action should get and calculate current time<-----')

    def action(self):
        pass
