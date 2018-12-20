#! /usr/bin/python
# -*- coding:utf-8 -*-

from com.forum.lottery.utils.Report import FileHelper

class NotSuccessException(Exception):
    def __init__(self, message):
        print(message)
        helper = FileHelper()
        helper.write(message)
