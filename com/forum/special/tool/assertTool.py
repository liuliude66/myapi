#! /usr/bin/python
# -*- coding:utf-8 -*-

# 判断code值
def assertCode(exceptCode, resultCode):
    if int(exceptCode) == resultCode:
        return {'code': 0, 'result' : 'pass'}
    else:
        return {'code': 1, 'result': 'failure'}