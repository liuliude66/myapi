#! /usr/bin/python
# -*- coding:utf-8 -*-

class SinglePay(object):

    __bankOder = {}   # 银行入款
    __thirdOrder = {}  # 第三方入款
    __preOrder = {}  # 固码入款

    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(SinglePay, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def setBankOder(self, bankOder):
        self.__bankOder = bankOder

    def getBankOder(self):
        return self.__bankOder

    def setThirdOrder(self, thirdOrder):
        self.__thirdOrder = thirdOrder

    def getThirdOrder(self):
        return self.__thirdOrder

    def setPreOrder(self, preOrder):
        self.__preOrder = preOrder

    def getPreOrder(self):
        return self.__preOrder
