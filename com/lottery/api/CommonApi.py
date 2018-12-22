#! /usr/bin/python
# -*- coding:utf-8 -*-

from __future__ import unicode_literals
import json
import requests

from com.lottery.api.Api import Api
from com.public.singleton import Singleton
from com.public.singlePay import SinglePay
from com.public.singleMange import SingleManage

# 模板Api接口
class CommonApi(Api):

    def __init__(self, url, parameter, case_name, expect, formData, index):
        Api.__init__(self)
        self.url = self.domain + url
        self.parameter = parameter
        self.case_name = case_name
        self.expect = expect
        self.formData = formData
        self.index = index

    def action(self):
        self.judgeHeader()
        session = requests.session()
        if 'login.do' in self.url:
            self.requestSessionid(session)
        format, result = self.jugdeParams()
        if format == 'data':
            response = session.post(self.url, headers=self.header, data=self.parameter, timeout=self.timeout, verify=False)
        elif format == 'json':
            response = session.post(self.url, headers=self.header, json=result, timeout=self.timeout, verify=False)
        self.api_response = json.loads(response.text)
        self.requestTime = response.elapsed.microseconds / 1000
        self.jugdeResponse(self.api_response)
        return self.api_response

    def judgeHeader(self):  # 处理请求头
        if self.formData == 1:
            self.header['content-type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
        else:
            self.header['content-type'] = 'application/json;charset:utf-8'

        if Singleton().getSessionId():
            self.header['sessionid'] = Singleton().getSessionId()

    def requestSessionid(self, session):  # 请求sessionid
        distribute = self.domain + '/passport/distribute_sessionid.do'
        distribute_r = session.post(distribute, headers=self.header, timeout=self.timeout, verify=False)
        distribute_response = json.loads(distribute_r.text)
        sessionid = distribute_response['data']['sessionid']
        Singleton().setSessionId(sessionid)
        self.judgeHeader()

    def jugdeParams(self):  # 请求参数替换本地数据
        if self.parameter:
            if self.formData == 0:
                if '/front/bet/betting.do' in self.url:
                    betParams = eval(self.parameter)
                    betParams['issue'] = str(int(Singleton().getBetIssue()) - 1)
                    return 'json', [betParams]
                else:
                    json_temp = eval(self.parameter)
                    json_temp = self.judgeManageParams(json_temp)
                    json_temp = self.judgePcParams(json_temp)

                    if 'userId' in json_temp.keys():
                        if Singleton().getUserId():
                            json_temp['userId'] = Singleton().getUserId()

                    self.parameter = json.dumps(json_temp)
                    return 'data', []
            else:
                list = self.parameter.split('&')
                files = dict()
                for listStr in list:
                    files[listStr.split('=')[0]] = (None, listStr.split('=')[1])
                self.judgeFormData(files)
                self.parameter = files
                return 'data', []
        else:
            return 'data', []

    def judgeManageParams(self, json):
        # 新闻
        if '/manage/news/get_detail.do' in self.url:
            if 'id' in json.keys():
                json['id'] = SingleManage().getNewId()

        if '/manage/news/add_or_update.do' in self.url:
            if 'id' in json.keys():
                json['id'] = SingleManage().getNewId()

        if '/manage/news/delete.do' in self.url:
            if 'id' in json.keys():
                json['id'] = SingleManage().getNewId()

        # 优惠活动
        if '/manage/discountoff/update_sort.do' in self.url:
            if 'discountoffId' in json.keys():
                json['discountoffId'] = SingleManage().getDiscountoffId()

        if '/manage/discountoff/get.do' in self.url:
            if 'discountoffId' in json.keys():
                json['discountoffId'] = SingleManage().getDiscountoffId()

        if '/manage/discountoff/update.do' in self.url:
            if 'discountoffId' in json.keys():
                json['discountoffId'] = SingleManage().getDiscountoffId()

        if '/manage/discountoff/delete.do' in self.url:
            if 'discountoffId' in json.keys():
                json['discountoffId'] = SingleManage().getDiscountoffId()

        return json

    def judgePcParams(self, json):
        if '/front/recharge/deposit_third.do' in self.url:
            if SinglePay().getThirdOrder():
                thirdOrder = SinglePay().getThirdOrder()
                json['thirdCode'] = thirdOrder['thirdCode']
                json['thirdMode'] = thirdOrder['thirdMode']
                json['thirdId'] = thirdOrder['id']

        if '/front/recharge/deposit_common.do' in self.url:
            if SinglePay().getBankOder():
                bankOrder = SinglePay().getBankOder()
                json['bankId'] = bankOrder['id']

        if '/front/recharge/preOrder.do' in self.url:
            if SinglePay().getPreOrder():
                preOrder = SinglePay().getPreOrder()
                json['thirdCode'] = preOrder['thirdCode']
                json['thirdMode'] = preOrder['thirdMode']
                json['thirdId'] = preOrder['id']
                json['receiveAccount'] = preOrder['receiveAccount']
                json['receiveName'] = preOrder['receiveName']
                json['payType'] = preOrder['payType']
        return json

    def judgeFormData(self, dict):  # formData请求参数替换本地数据
        if '/passport/login_validate.do' in self.url:
            if 'accessToken' in dict.keys():
                dict['accessToken'] = (None, Singleton().getAccessToken())
        return dict

    def jugdeResponse(self, response):  # 返回值存到本地
        if 'login.do' in self.url:
            if 'userId' in response['data']:
                Singleton().setUserId(response['data']['userId'])

        if '/front/bet/betting.do' in self.url:
            if 'data' in response.keys():
                Singleton().setOrderId(response['data'])

        if '/front/interface/draw_info.do' in self.url:
            if 'currentIssue' in response['data'].keys():
                Singleton().setBetIssue(response['data']['currentIssue'])

        if '/passport/manage_login.do' in self.url:
            if 'data' in response.keys():
                Singleton().setAccessToken(response['data'])

        self.judgeManageResponse(response)
        self.judgePcResponse(response)

    def judgeManageResponse(self, response):
        # 新闻
        if '/manage/news/get_list.do' in self.url:
            if 'rows' in response.keys():
                item = response['rows'][0]
                SingleManage().setNewId(item['id'])

        # 优惠活动
        if '/manage/discountoff/list.do' in self.url:
            if 'rows' in response.keys():
                item = response['rows'][0]
                SingleManage().setDiscountoffId(item['discountoffId'])

    def judgePcResponse(self, response):
        # 充值方式
        if '/front/recharge/get_deposit_list.do' in self.url:
            if 'data' in response.keys():
                list = response['data']
                bankOrder = dict()
                thirdOrder = dict()
                preOrder = dict()
                for item in list:
                    if item['type'] == 'bank':
                        if SinglePay().getBankOder():
                            continue
                        bankOrder['bankId'] = item['id']
                        SinglePay().setBankOder(bankOrder)
                    else:
                        subList = item['payways']
                        for subItem in subList:
                            if subItem['payType'] == 'online':
                                if SinglePay().getThirdOrder():
                                    continue
                                thirdOrder['thirdCode'] = subItem['thirdCode']
                                thirdOrder['thirdMode'] = subItem['thirdMode']
                                thirdOrder['thirdId'] = subItem['id']
                                SinglePay().setThirdOrder(thirdOrder)
                            elif subItem['payType'] == 'SELF':
                                if SinglePay().getPreOrder():
                                    continue
                                preOrder['thirdCode'] = subItem['thirdCode']
                                preOrder['thirdMode'] = subItem['thirdMode']
                                preOrder['thirdId'] = subItem['id']
                                preOrder['receiveAccount'] = subItem['receiveAccount']
                                preOrder['receiveName'] = subItem['receiveName']
                                preOrder['payType'] = subItem['payType']
                                SinglePay().setPreOrder(preOrder)
