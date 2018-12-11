#! /usr/bin/python
# -*- coding:utf-8 -*-

class Singleton(object):

    __sessionid = ''

    __instance = None
    def __new__(cls, *args, **kwargs):  # 这里不能使用__init__，因为__init__是在instance已经生成以后才去调用的
        if cls.__instance is None:
            cls.__instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls.__instance


    def setSessionId(self, sessionId):
        self.__sessionid = sessionId


    def getSessionId(self):
        return self.__sessionid
