#! /usr/bin/python
# -*- coding:utf-8 -*-
import json

import requests

from com.forum.lottery.api.Api import Api
from com.forum.lottery.common.NotSuccessException import NotSuccessException
from com.forum.lottery.common.Singleton import Singleton


class LoginApi(Api):

    def __init__(self, username, password):
        Api.__init__(self)
        self.url = self.domain + 'passport/distribute_sessionid.do'
        self.login = self.domain + 'passport/login.do'
        self.parameter['account'] = username
        self.parameter['password'] = password

    def action(self):
        session = requests.session()
        response = session.post(self.url, headers=self.header, data=self.parameter, timeout=self.timeout)
        res = json.loads(response.text)
        if res['code'] == 0:    # 开始执行登录操作
            sessionid = res['data']['sessionid']
            self.header['sessionid'] = sessionid
            instance = Singleton()
            instance.setSessionId(sessionid)
            params = json.dumps(self.parameter)
            response = session.post(self.login, headers=self.header, data=params, timeout=self.timeout)
            print(response.text)
            login_res = json.loads(response.text)
            if login_res['code'] != 0:
                content = self.login + "\n" + res['msg']
                raise NotSuccessException(content)
            else:
                instance.setUserId(login_res['data']['userId'])
        else:
            content = self.url + "\n" + res['msg']
            raise NotSuccessException(content)

