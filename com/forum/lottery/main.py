#! python
# -*- coding:utf-8 -*-
from com.forum.lottery.utils.ExcelManager import *
from com.forum.lottery.utils.HtmlManager import *
from com.forum.lottery.api.CommonApi import CommonApi
from com.forum.lottery.utils.Report import FileHelper

if __name__ == '__main__':
    print("------->  start  <-------")
    create_html_file()
    helper = FileHelper()
    helper.write(generate_html_head())
    cases = read_excel()
    start = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    for item in cases:
        CommonApi(item['request_url'], item['parameter'], item['case_name'], item['request_expect']).run()
    end = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    summarize = summarize_html(start, end, GlobalConfig['SUCCESS_COUNT'], GlobalConfig['FAILURE_COUNT'], GlobalConfig['UNKNOWN_COUNT'], GlobalConfig['ERROR_COUNT'])
    helper.write(summarize)
    helper.write(generate_html_tail())
    print("------->  over  <-------")
