#! /usr/bin/python
# -*- coding:utf-8 -*-

from com.forum.special.service.serviceTool import Request
from com.forum.special.service.urlService import LoginModule
from com.forum.public.singleton import Singleton

requset = Request()

class LoginHttpTool(object):
    @classmethod
    def postGetSessionid(cls): # 请求sessionId
        success, json = requset.post(LoginModule.urlSessionId, None)
        if success == 0:
            if json['code'] == 0:
                Singleton().setSessionId(json['data']['sessionid'])
                return 0, json
            else:
                return json['code'], json
        else:
            return 1, json

    @classmethod
    def postRegisterOption(cls): # 获取注册选项
        success, json = requset.post(LoginModule.urlRegisterOptions, None)
        if success == 0:
            if json['code'] == 0:
                return 0, json
            else:
                return json['code'], json
        else:
            return 1, json

    @classmethod
    def postRegister(cls, param): # 注册
        success, json = requset.post(LoginModule.urlRegister, param)
        if success == 0:
            if json['code'] == 0:
                return 0, json
            else:
                return json['code'], json
        else:
            return 1, json

    @classmethod
    def postLogin(cls, param): # 登录
        success, json = requset.post(LoginModule.urlLogin, param)
        if success == 0:
            if json['code'] == 0:
                return 0, json
            else:
                return json['code'], json
        else:
            return 1, json

    @classmethod
    def postLogout(cls): # 退出
        success, json = requset.post(LoginModule.urlLogout, None)
        if success == 0:
            if json['code'] == 0:
                return 0, json
            else:
                return json['code'], json
        else:
            return 1, json

