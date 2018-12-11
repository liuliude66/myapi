#! /usr/bin/python
# -*- coding:utf-8 -*-

import json
import requests

from com.forum.lottery.api.Api import Api
from com.forum.lottery.common.NotSuccessException import NotSuccessException
from com.forum.lottery.common.Singleton import Singleton


# 开奖Api接口
class LotteryApi(Api):

    def __init__(self):
        Api.__init__(self)
        self.url = self.domain + 'front/lottery/luck_number.do'
        instance = Singleton()
        self.header['sessionid'] = instance.getSessionId()

    def action(self):
        session = requests.session()
        response = session.post(self.url, headers=self.header, timeout=self.timeout)
        res = json.loads(response.text)
        print(res)
        if res['code'] != 0:  # 开始执行登录操作
            content = self.url + "\n" + res['msg']
            raise NotSuccessException(content)