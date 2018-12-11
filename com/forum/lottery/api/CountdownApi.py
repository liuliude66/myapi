#! /usr/bin/python
# -*- coding:utf-8 -*-


import requests
import json
from com.forum.lottery.api.Api import Api
from com.forum.lottery.common.Singleton import Singleton


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
        if res['code'] == 0:    # 开始执行登录操作
            print(response.text)
        else:
            print(res['code'])
            print('即将写入报告，是否成功')
