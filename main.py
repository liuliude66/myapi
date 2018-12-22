#! python
# -*- coding:utf-8 -*-

from __future__ import unicode_literals
from com.lottery.api.CommonApi import CommonApi
from com.lottery.utils.Report import FileHelper
from com.tool.transTool import TransTool
from com.tool.testConfig import TestConfig
from com.config.globalConfig import GlobalConfig
from com.lottery.utils.HtmlManager import *

def handleTestData(items, fileName):
    print("------->  start  <-------")
    GlobalConfig['SUCCESS_COUNT'], GlobalConfig['FAILURE_COUNT'], GlobalConfig['EXCEPTION_COUNT'], GlobalConfig['ERROR_COUNT'] = 0, 0, 0, 0
    create_html_file(fileName)
    helper = FileHelper()
    helper.write(generate_html_head())
    start = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    for i in range(len(items)):
        item = items[i]
        if item['test_switch'] != '是':
            continue
        formData = 0
        if 'isFormData' in item.keys():
            if item['isFormData'] == '是':
                formData = 1
        CommonApi(item['request_url'], item['parameter'], item['case_name'], item['request_expect'], formData, i).run()
    end = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    summarize = summarize_html(start, end, GlobalConfig['SUCCESS_COUNT'], GlobalConfig['FAILURE_COUNT'], GlobalConfig['EXCEPTION_COUNT'], GlobalConfig['ERROR_COUNT'])
    helper.write(summarize)
    helper.write(generate_html_tail())
    print("------->  end  <-------")

def start_interface_html_http():
    # app接口测试
    handleTestData(TransTool().TransSpecial(TestConfig().getAllInterfaceData('interface_app', 'app接口测试')), 'app接口测试')

    # 代理接口测试
    handleTestData(TransTool().TransSpecial(TestConfig().getAllInterfaceData('interface_agent_mobile', '代理接口测试')), '代理接口测试')

    # 后台管理测试
    handleTestData(TransTool().TransSpecial(TestConfig().getFormModuleInterfaceData('interface_manage', '后台管理接口测试')), '后台管理接口测试')

    # pc接口测试
    handleTestData(TransTool().TransSpecial(TestConfig().getFormModuleInterfaceData('interface_pc', 'pc接口测试')), 'pc接口测试')

if __name__ == '__main__':
    start_interface_html_http()

