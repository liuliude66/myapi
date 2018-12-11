#! /usr/bin/python
# -*- coding:utf-8 -*-

import json
import requests

from com.forum.lottery.api.Api import Api
from com.forum.lottery.common.NotSuccessException import NotSuccessException
from com.forum.lottery.common.Singleton import Singleton


# 充值记录Api接口
class RechargeRecordApi(Api):

    def __init__(self):
        Api.__init__(self)
        self.url = self.domain + 'capital/manage/change_log.do'
        instance = Singleton()
        self.header['sessionid'] = instance.getSessionId()
        self.parameter['page'] = 1
        self.parameter['type'] = -1


    def action(self):
        session = requests.session()
        params = json.dumps(self.parameter)
        response = session.post(self.url, headers=self.header, data=params, timeout=self.timeout)
        res = json.loads(response.text)
        print(res)
        if res['code'] != 0:  # 开始执行登录操作
            content = self.url + "\n" + res['msg']
            raise NotSuccessException(content)
