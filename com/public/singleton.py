#! /usr/bin/python
# -*- coding:utf-8 -*-

class Singleton(object):

    __sessionid = ''
    __version = '5.2.3'
    __userid = ''
    __access_token = ''
    __orderId = ''
    __betIssue = ''

    __instance = None
    def __new__(cls, *args, **kwargs):  # 这里不能使用__init__，因为__init__是在instance已经生成以后才去调用的
        if cls.__instance is None:
            cls.__instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def setSessionId(self, sessionId):
        self.__sessionid = sessionId

    def getSessionId(self):
        return self.__sessionid

    def setAccessToken(self, access_token):
        self.__access_token = access_token

    def getAccessToken(self):
        return self.__access_token

    def setUserId(self, __userid):
        self.__userid = __userid

    def getUserId(self):
        return self.__userid

    def getVersion(self):
        return self.__version

    def setOrderId(self, orderId):
        self.__orderId = orderId

    def getOrderId(self):
        return self.__orderId

    def setBetIssue(self, betIssue):
        self.__betIssue = betIssue

    def getBetIssue(self):
        return self.__betIssue
