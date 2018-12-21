#! python
# -*- coding:utf-8 -*-

from __future__ import unicode_literals
from com.forum.lottery.utils.HtmlManager import *
from com.forum.lottery.api.CommonApi import CommonApi
from com.forum.lottery.utils.Report import FileHelper
from com.forum.tool.transTool import TransTool
from com.forum.tool.testConfig import TestConfig

def handleTestData(items, fileName):
    print("------->  start  <-------")
    GlobalConfig['SUCCESS_COUNT'], GlobalConfig['FAILURE_COUNT'], GlobalConfig['EXCEPTION_COUNT'], GlobalConfig['ERROR_COUNT'] = 0, 0, 0, 0
    create_html_file(fileName)
    helper = FileHelper()
    helper.write(generate_html_head())
    start = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    for item in items:
        print(item)
        if item['test_switch'] != '是':
            continue
        CommonApi(item['request_url'], item['parameter'], item['case_name'], item['request_expect']).run()
    end = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    summarize = summarize_html(start, end, GlobalConfig['SUCCESS_COUNT'], GlobalConfig['FAILURE_COUNT'], GlobalConfig['EXCEPTION_COUNT'], GlobalConfig['ERROR_COUNT'])
    helper.write(summarize)
    helper.write(generate_html_tail())
    print("------->  end  <-------")

def start_interface_html_http():
    # app接口测试
    # handleTestData(TransTool().TransSpecial(TestConfig().getAllInterfaceData('interface_app', 'app接口测试')), 'app接口测试')

    # 代理接口测试
    handleTestData(TransTool().TransSpecial(TestConfig().getAllInterfaceData('interface_agent_mobile', '代理接口测试')), '代理接口测试')

if __name__ == '__main__':
    start_interface_html_http()

