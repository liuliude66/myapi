#! /usr/bin/python
# -*- coding:utf-8 -*-

import json
import requests

from com.forum.lottery.api.Api import Api
from com.forum.lottery.config.GlobalParams import GlobalConfig


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
        if '/passport/login.do' in self.url:
            distribute = self.domain + '/passport/distribute_sessionid.do'
            distribute_r = session.post(distribute, headers=self.header, timeout=self.timeout)
            distribute_response = json.loads(distribute_r.text)
            GlobalConfig['SESSION_ID'] = distribute_response['data']['sessionid']
            self.header['sessionid'] = GlobalConfig['SESSION_ID']
            login_r = session.post(self.url, headers=self.header, data=self.parameter, timeout=self.timeout)
            login_response = json.loads(login_r.text)
            GlobalConfig['USER_ID'] = login_response['data']['userId']
            self.api_response = login_response
        else:
            self.header['sessionid'] = GlobalConfig['SESSION_ID']
            # if self.parameter:
            #     json_temp = eval(self.parameter)
            #     json_temp['userid'] = GlobalConfig['USER_ID']
            #     self.parameter = json.dumps(json_temp)
            response = session.post(self.url, headers=self.header, data=self.parameter, timeout=self.timeout)
            self.api_response = json.loads(response.text)
            # if res['code'] != 0:  # 开始执行登录操作
            #     content = self.url + "\n" + res['msg']
            #     raise NotSuccessException(content)
        return self.api_response
