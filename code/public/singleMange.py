#! /usr/bin/python
# -*- coding:utf-8 -*-

class SingleManage(object):

    __newId = ''   # 新闻id
    __discountoffId = ''  # 活动id

    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(SingleManage, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def setNewId(self, newId):
        self.__newId = newId

    def getNewId(self):
        return self.__newId

    def setDiscountoffId(self, discountoffId):
        self.__discountoffId = discountoffId

    def getDiscountoffId(self):
        return self.__discountoffId