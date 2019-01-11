#! python
# -*- coding:utf-8 -*-

from __future__ import unicode_literals

from code.interface.api.CommonApi import CommonApi
from code.interface.utils.Report import FileHelper
from code.tool.transTool import TransTool
from code.tool.testConfig import TestConfig
from code.interface.utils.HtmlManager import *
from code.special.testCase.loginTest import LoginTest

def handleTestData(items, fileName):
    print("------->  start  <-------")
    GlobalConfig.Success_count, GlobalConfig.Failure_count, GlobalConfig.Exception_count, GlobalConfig.Error_count = 0, 0, 0, 0
    create_html_file(fileName)
    helper = FileHelper()
    helper.write(generate_html_head())
    start = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    for i in range(len(items)):
        item = items[i]
        if item['test_switch'] != '是':
            continue
        formData = 0
        if 'isFormData' in item:
            if item['isFormData'] == '是':
                formData = 1
        CommonApi(item['request_url'], item['parameter'], item['case_name'], item['request_expect'], formData, i).run()
    end = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    summarize = summarize_html(start, end, GlobalConfig.Success_count, GlobalConfig.Failure_count, GlobalConfig.Exception_count, GlobalConfig.Error_count)
    helper.write(summarize)
    helper.write(generate_html_tail())
    print("------->  end  <-------")

def start_interface_html_http():
    # app接口测试
    # handleTestData(TransTool().TransSpecial(TestConfig().getAllInterfaceData('interface_app', 'app接口测试')), 'app接口测试')

    # 代理接口测试
    # handleTestData(TransTool().TransSpecial(TestConfig().getAllInterfaceData('interface_agent_mobile', '代理接口测试')), '代理接口测试')

    # 后台管理测试
    handleTestData(TransTool().TransSpecial(TestConfig().getFormModuleInterfaceData('interface_manage', '后台管理接口测试')), '后台管理接口测试')

    # pc接口测试
    # handleTestData(TransTool().TransSpecial(TestConfig().getFormModuleInterfaceData('interface_pc', 'pc接口测试')), 'pc接口测试')

if __name__ == '__main__':
    # start_interface_html_http()
    try:
        LoginTest().specialRegisteCase()
    except Exception as ex:
        print(ex.args)

