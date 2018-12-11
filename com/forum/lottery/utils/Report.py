#! /usr/bin/python
# -*- coding:utf-8 -*-

class FileHelper(object):

    file = 'report.txt'

    def __init__(self):
        pass

    def write(self, content):
        fo = None
        try:
            fo = open(self.file, "a+")
            if isinstance(content, str):
                fo.write(content + "\n")
            elif isinstance(content, tuple):
                fo.write(str(tuple(content)) + "\n")
        finally:
            if not fo:
                fo.close()
