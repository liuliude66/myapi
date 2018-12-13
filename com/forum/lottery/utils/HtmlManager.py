#! /usr/bin/python
# -*- coding:utf-8 -*-
import time
from com.forum.lottery.config.GlobalParams import GlobalConfig


# 创建HTML文档
def create_html_file():
    localtime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    GlobalConfig['REPORT_PATH'] = GlobalConfig['REPORT_PATH'] + localtime + ".html"
    print(GlobalConfig['REPORT_PATH'])


def generate_html_head():
    return '''<!DOCTYPE html>
    <html>
    <head>
        <title>测试结果</title>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8″>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <!-- 引入 Bootstrap -->
        <link href="https://cdn.bootcss.com/bootstrap/3.3.6/css/bootstrap.min.css" rel="stylesheet">
        <!-- HTML5 Shim 和 Respond.js 用于让 IE8 支持 HTML5元素和媒体查询 -->
        <!-- 注意： 如果通过 file://  引入 Respond.js 文件，则该文件无法起效果 -->
        <!--[if lt IE 9]>
         <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
         <script src="https://oss.maxcdn.com/libs/respond.js/1.3.0/respond.min.js"></script>
        <![endif]-->
        <style type="text/css">
            .hidden-detail,.hidden-tr{
                display:none;
            }
        </style>
    </head>
    <body>
        <div class="row " style="margin:6px">
            <div style='margin-top: 1%;' >
                <div class="btn-group" role="group" aria-label="...">
                    <button type="button" id="check-all" class="btn btn-primary">所有用例</button>
                    <button type="button" id="check-success" class="btn btn-success">成功用例</button>
                    <button type="button" id="check-danger" class="btn btn-danger">失败用例</button>
                    <button type="button" id="check-warning" class="btn btn-warning">错误用例</button>
                    <button type="button" id="check-except" class="btn btn-defult">异常用例</button>
                </div>
            <div class="btn-group" role="group" aria-label="..."></div>
            <table class="table table-hover table-condensed table-bordered" style="word-wrap:break-word; word-break:break-all;  margin-top: 7px; table-layout: fixed;">
                <tr style='text-align:center;'>
                    <td class='col-md-1'><strong>用例名字</strong></td>
                    <td class='col-md-2'><strong>请求参数</strong></td>
                    <td class='col-md-3'><strong>url</strong></td>
                    <td class='col-md-1'><strong>预期</strong></td>
                    <td class='col-md-4'><strong>实际返回</strong></td>  
                    <td class='col-md-1'><strong>结果</strong></td>
                </tr>
    '''


def summarize_html(start, end, pass_count, fail_count, exception_count, error_count):
    start_t = int(time.mktime(time.strptime(start, "%Y-%m-%d %H:%M:%S")))
    end_t = int(time.mktime(time.strptime(end, "%Y-%m-%d %H:%M:%S")))
    return '''
        <div><table  class="table table-hover table-condensed">
            <tbody>
                <tr><td><strong>开始时间:</strong> %s</td></tr>
                <tr><td><strong>结束时间:</strong> %s</td></tr>
                <tr><td><strong>耗时:</strong> %s 秒</td></tr>
                <tr>
                    <td>
                        <strong>结果:</strong>
                        <span >
                            通过: <strong >%s</strong>  
                            失败: <strong >%s</strong>
                            执行异常: <strong >%s</strong>
                            未知错误: <strong >%s</strong></span>
                    </td>                  
                </tr> 
            </tbody>
		</table></div> ''' % (start, end, (end_t - start_t), pass_count, fail_count, exception_count, error_count)


def pass_result(tend):
    if tend == 'pass':
        htl = '''<td bgcolor="green" style="text-align:center;color:white;">成功</td>'''
    elif tend == 'fail':
        htl = '''<td bgcolor="red" style="text-align:center;">失败</td>'''
    elif tend == 'exception':
        htl = '''<td bgcolor="yellow" style="text-align:center;">执行异常</td>'''
    else:
        htl = '<td bgcolor="crimson" style="text-align:center;">输入期望值</td>'
    return htl


def generate_html_tail():
    return '''</div></div></table><script src="https://code.jquery.com/jquery.js"></script>
    <script src="https://cdn.bootcss.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
    <script type="text/javascript">
    	$("#check-danger").click(function(e){
    	    $(".case-tr").removeClass("hidden-tr");
            $(".success").addClass("hidden-tr");
            $(".warning").addClass("hidden-tr");
            $(".error").addClass("hidden-tr");
    	});
    	$("#check-warning").click(function(e){
    		 $(".case-tr").removeClass("hidden-tr");
            $(".success").addClass("hidden-tr");
            $(".danger").addClass("hidden-tr");
            $(".error").addClass("hidden-tr");
    	});
    	$("#check-success").click(function(e){
    		 $(".case-tr").removeClass("hidden-tr");
            $(".warning").addClass("hidden-tr");
            $(".danger").addClass("hidden-tr");
            $(".error").addClass("hidden-tr");
    	});
    	$("#check-except").click(function(e){
    		 $(".case-tr").removeClass("hidden-tr");
            $(".warning").addClass("hidden-tr");
            $(".danger").addClass("hidden-tr");
            $(".success").addClass("hidden-tr");
    	});
    	$("#check-all").click(function(e){
    	    $(".case-tr").removeClass("hidden-tr");
    	});
    </script>
    </body></html>'''


def generate_html_file(header, case_name, url, parameter, expect, real, result):
    return '''
    <tr class="case-tr %s">
        <td style='text-align:center;'>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td style='text-align:center;'>%s</td>
        <td style="overflow: hidden;text-overflow: ellipsis;word-break:break-all;word-wrap:break-word;white-space: nowrap;">%s</td>
        %s
    </tr>
    ''' % (header, case_name, parameter, url, expect, real, pass_result(result))
