#! /usr/bin/python
# -*- coding:utf-8 -*-

OutputName = 'outputName'
ExcelName = 'excelName'
ExcelItem = 'excelItem'
ParamList = 'paramList'
PostParamList = 'postParamList'
PostParam = 'postParam'
ExtraResult = 'extraResult'

class TestConfig():
    @classmethod
    def getRegisteData(cls): # 注册相关测试
        return {
            OutputName: '注册',
            ExcelName: 'special_register',
            ExcelItem: ['编号', '账号', '密码', '真实姓名', 'QQ', '手机号', '邀请码', '微信', '是否成立', '预期成功', '执行人', '备注'],
            ParamList: ['id', 'account', 'password', 'realName', 'qq', 'phone', 'referer', 'wechat', 'isFound', 'except','user', 'remark'],
            PostParamList: ['account', 'password', 'realName', 'qq', 'phone', 'referer', 'wechat'],
            ExtraResult: ['返回结果', '是否通过', '请求时长(ms)']
        }

    @classmethod
    def getLoginData(cls): # 登录相关测试
        return {
            OutputName: '登录',
            ExcelName: 'special_login',
            ExcelItem: ['编号', '账号', '密码', '是否成立', '预期成功', '执行人', '备注'],
            ParamList: ['id', 'account', 'password', 'isFound', 'except', 'user', 'remark'],
            PostParamList: ['account', 'password'],
            ExtraResult: ['返回结果', '是否通过', '请求时长(ms)']
        }

    @classmethod
    def getNormalInterfaceData(cls, name):  # 通用接口测试
        return {
            OutputName: name,
            ExcelItem: ['编号', '接口名称', 'url', '参数', '是否登录'],
            ParamList: ['id', 'name', 'url', 'params', 'isLogin'],
            ExtraResult: ['返回结果', '是否通过', '请求时长(ms)']
        }

    @classmethod
    def getRegisteInterfaceData(cls):  # 注册接口测试
        return {
            OutputName: '注册',
            ExcelItem: ['编号', '接口名称', 'url'],
            ParamList: ['id', 'name', 'url'],
            ExtraResult: ['返回结果', '是否通过', '请求时长(ms)'],
            PostParam: {'account': 'well', 'password': '123123'}
        }

    @classmethod
    def getLoginInterfaceData(cls): # 登录接口测试
        return {
            OutputName: '登录',
            ExcelItem: ['编号', '接口名称', 'url'],
            ParamList: ['id', 'name', 'url'],
            ExtraResult: ['返回结果', '是否通过', '请求时长(ms)'],
            PostParam: {'account': 'well', 'password': '123123'}
        }

    @classmethod
    def getBetInterfaceData(cls): # 投注布局接口测试
        return {
            OutputName: '投注',
            ExcelItem: ['编号', '接口名称', 'url', '参数', '是否登录'],
            ParamList: ['id', 'name', 'url', 'params', 'isLogin'],
            ExtraResult: ['返回结果', '是否通过', '请求时长(ms)']
        }

    @classmethod
    def getBetContentData(cls, lottery):  # 投注下注接口测试
        return {
            OutputName: lottery,
            ExcelItem: ['编号', '下注内容', '下注金额', '追期期数', '是否成立', '预期成功', '执行人', '备注'],
            ParamList: ['id', 'name', 'url', 'params', 'isLogin'],
            ExtraResult: ['url', '请求参数', '是否登录', '返回结果', '是否通过', '请求时长(ms)']
        }