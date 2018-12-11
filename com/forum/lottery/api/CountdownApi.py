#! /usr/bin/python
# -*- coding:utf-8 -*-


import requests
import json
from com.forum.lottery.api.Api import Api
from com.forum.lottery.common.Singleton import Singleton
from com.forum.lottery.common.NotSuccessException import NotSuccessException


class CountdownApi(Api):

    def __init__(self):
        Api.__init__(self)
        self.url = self.domain + 'front/lottery/init.do'
        instance = Singleton()
        self.header['sessionid'] = instance.getSessionId()

    def action(self):
        session = requests.session()
        response = session.post(self.url, headers=self.header, timeout=self.timeout)
        res = json.loads(response.text)
        print(res)
        if res['code'] != 0:    # 开始执行Api判断操作
            content = self.url + "\n" + res['msg']
            raise NotSuccessException(content)
