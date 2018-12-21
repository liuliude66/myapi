#! /usr/bin/python
# -*- coding:utf-8 -*-

from __future__ import unicode_literals
import json
import requests

from com.forum.lottery.api.Api import Api
from com.forum.public.singleton import Singleton
from com.forum.special.service.urlService import *

# 模板Api接口
class AdminCommonApi(Api):

    def __init__(self, url, parameter, case_name, expect):
        Api.__init__(self)
        self.url = self.domain + url
        self.parameter = parameter
        self.case_name = case_name
        self.expect = expect

    def action(self):
        session = requests.session()
        if 'login.do' in self.url:
            distribute = self.domain + '/passport/distribute_sessionid.do'
            distribute_r = session.post(distribute, headers=self.header, timeout=self.timeout, verify=False)
            distribute_response = json.loads(distribute_r.text)
            sessionid = distribute_response['data']['sessionid']
            Singleton().setSessionId(sessionid)
            self.header['sessionid'] = sessionid
            print("sessionid--->" + sessionid)
            if self.parameter:
                json_temp = eval(self.parameter)
                self.parameter = json.dumps(json_temp)
            login_r = session.post(self.url, headers=self.header, data=self.parameter, timeout=self.timeout, verify=False)
            login_response = json.loads(login_r.text)
            login_data = login_response['data']
            print("login_data--->" + login_data)
            if isinstance(login_data, dict):
                userId = login_response['data']['userId']
                Singleton().setUserId(userId)
            elif isinstance(login_data, str):
                Singleton().setAccessToken(login_data)
            self.api_response = login_response
            self.requestTime = login_r.elapsed.microseconds / 1000
        elif '/passport/login_validate.do' in self.url:
            self.header['content-type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
            self.header['sessionid'] = Singleton().getSessionId()
            parameter = dict()
            parameter['accessToken'] = Singleton().getAccessToken()
            parameter['code'] = '1111'
            response = session.post(self.url, headers=self.header, data=parameter, timeout=self.timeout, verify=False)
            self.api_response = json.loads(response.text)
            self.requestTime = response.elapsed.microseconds / 1000
        elif 'user_info.do' in self.url or 'get_register_log.do' in self.url or 'get_logined_log.do' in self.url:
            self.header['content-type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
            self.header['sessionid'] = Singleton().getSessionId()
            if self.parameter:
                self.parameter = eval(self.parameter)
            parameter = self.parameter
            parameter['accessToken'] = Singleton().getAccessToken()
            response = session.post(self.url, headers=self.header, data=parameter, timeout=self.timeout, verify=False)
            self.api_response = json.loads(response.text)
            self.requestTime = response.elapsed.microseconds / 1000
        else:
            self.header['content-type'] = 'application/json;charset:utf-8'
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

        return self.api_response
