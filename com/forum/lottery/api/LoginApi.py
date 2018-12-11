#! /usr/bin/python
# -*- coding:utf-8 -*-
import requests
import json
from com.forum.lottery.api.Api import Api
from com.forum.lottery.common.Singleton import Singleton


class LoginApi(Api):

    def __init__(self, username, password):
        Api.__init__(self)
        self.url = self.domain + 'passport/distribute_sessionid.do'
        self.login = self.domain + 'passport/login.do'
        self.parameter['account'] = username
        self.parameter['password'] = password

    def action(self):
        print('-----------> start login test <-----------')
        session = requests.session()
        response = session.post(self.url, headers=self.header, data=self.parameter, timeout=self.timeout)
        res = json.loads(response.text)
        if res['code'] == 0:    # 开始执行登录操作
            sessionid = res['data']['sessionid']
            self.header['sessionid'] = sessionid
            intstance = Singleton()
            intstance.setSessionId(sessionid)
            params = json.dumps(self.parameter)
            response = session.post(self.login, headers=self.header, data=params, timeout=self.timeout)
            print(response.text)
        else:
            print(res['code'])
            print('即将写入报告，是否成功')

