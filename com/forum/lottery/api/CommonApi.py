#! /usr/bin/python
# -*- coding:utf-8 -*-

from __future__ import unicode_literals
import json
import requests

from com.forum.lottery.api.Api import Api
from com.forum.public.singleton import Singleton
from com.forum.special.service.urlService import *

# 模板Api接口
class CommonApi(Api):

    def __init__(self, url, parameter, case_name, expect):
        Api.__init__(self)
        self.url = self.domain + url
        self.parameter = parameter
        self.case_name = case_name
        self.expect = expect

    def action(self):
        session = requests.session()
        if LoginModule.urlLogin in self.url:
            distribute = self.domain + '/passport/distribute_sessionid.do'
            distribute_r = session.post(distribute, headers=self.header, timeout=self.timeout, verify=False)
            distribute_response = json.loads(distribute_r.text)
            sessionid = distribute_response['data']['sessionid']
            Singleton().setSessionId(sessionid)
            self.header['sessionid'] = sessionid
            if self.parameter:
                json_temp = eval(self.parameter)
                self.parameter = json.dumps(json_temp)
            login_r = session.post(self.url, headers=self.header, data=self.parameter, timeout=self.timeout, verify=False)
            login_response = json.loads(login_r.text)
            userId = login_response['data']['userId']
            Singleton().setUserId(userId)
            self.api_response = login_response
            self.requestTime = login_r.elapsed.microseconds / 1000
        else:
            self.header['sessionid'] = Singleton().getSessionId()
            if BetModule.urlBetBetting in self.url:
                items = [eval(self.parameter)]
                response = session.post(self.url, headers=self.header, json=items, timeout=self.timeout, verify=False)
                self.api_response = json.loads(response.text)
                self.requestTime = response.elapsed.microseconds / 1000
            else:
                if self.parameter:
                    json_temp = eval(self.parameter)
                    if 'userId' in json_temp.keys():
                        json_temp['userId'] = Singleton().getUserId()
                    self.parameter = json.dumps(json_temp)
                response = session.post(self.url, headers=self.header, data=self.parameter, timeout=self.timeout, verify=False)
                self.api_response = json.loads(response.text)
                self.requestTime = response.elapsed.microseconds / 1000

                # if res['code'] != 0:  # 开始执行登录操作
                #     content = self.url + "\n" + res['msg']
                #     raise NotSuccessException(content)
        return self.api_response
