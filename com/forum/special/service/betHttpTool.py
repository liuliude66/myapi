#! /usr/bin/python
# -*- coding:utf-8 -*-

from com.forum.special.service.serviceTool import Request
from com.forum.special.service.urlService import BetModule

requset = Request()

class BetHttpTool(object):
    @classmethod
    def postBetAllLottery(cls):
        success, json = requset.post(BetModule.urlBetAllLottery, None)
        if success == 0:
            if json['code'] == 0:
                return 0, json
            else:
                return json['code'], json
        else:
            return 1, json

    @classmethod
    def postBetPlayGroupItems(cls, lotteryId):
        success, json = requset.post(BetModule.urlBetPlayGroupItems, {'lotteryId': lotteryId})
        if success == 0:
            if json['code'] == 0:
                return 0, json
            else:
                return json['code'], json
        else:
            return 1, json

    @classmethod
    def postBetGetLayoutItem(cls, playId):
        success, json = requset.post(BetModule.urlBetGetLayoutItem, {'playId': playId})
        if success == 0:
            if json['code'] == 0:
                return 0, json
            else:
                return json['code'], json
        else:
            return 1, json

    @classmethod
    def postBetBetting(cls, items):
        success, json = requset.post(BetModule.urlBetBetting + '?after=1', items)
        if success == 0:
            if json['code'] == 0:
                return 0, json
            else:
                return json['code'], json
        else:
            return 1, json

    @classmethod
    def postBetBettingNextPeriod(cls, orderId):
        success, json = requset.post(BetModule.urlBetBettingNextPeriod, {'orderId': orderId})
        if success == 0:
            if json['code'] == 0:
                return 0, json
            else:
                return json['code'], json
        else:
            return 1, json

