#! /usr/bin/python
# -*- coding:utf-8 -*-
from com.forum.config.globalConfig import GlobalConfig

class FileHelper(object):

    def __init__(self):
        pass

    def write(self, content):
        fo = None
        try:
            fo = open(GlobalConfig['REPORT_PATH'], "a+")
            if isinstance(content, str):
                fo.write(content + "\n")
            elif isinstance(content, tuple):
                fo.write(str(tuple(content)) + "\n")
        finally:
            if not fo:
                fo.close()

