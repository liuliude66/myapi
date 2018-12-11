#! /usr/bin/python
# -*- coding:utf-8 -*-

import json
import requests

from com.forum.lottery.api.Api import Api
from com.forum.lottery.common.NotSuccessException import NotSuccessException
from com.forum.lottery.common.Singleton import Singleton


# 投注记录Api接口
class BetRecordApi(Api):

    def __init__(self):
        Api.__init__(self)
        self.url = self.domain + 'front/bet/log_list.do'
        instance = Singleton()
        self.header['sessionid'] = instance.getSessionId()
        self.parameter['status'] = -1 #  全部订单
        self.parameter['page'] = 1
        self.parameter['lotteryId'] = -1  #  全部彩种

    def action(self):
        session = requests.session()
        params = json.dumps(self.parameter)
        response = session.post(self.url, headers=self.header, data=params, timeout=self.timeout)
        res = json.loads(response.text)
        print(res)
        if res['code'] != 0:  # 开始执行登录操作
            content = self.url + "\n" + res['msg']
            raise NotSuccessException(content)
