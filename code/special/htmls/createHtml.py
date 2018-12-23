#! /usr/bin/python
# -*- coding:utf-8 -*-

import os, time, copy

from rootPath import getRootPath

titles = '接口测试'

def htmlTitle(titles):
    title = '''<!DOCTYPE html>
<htmls>
<head>
	<title>%s</title>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- 引入 Bootstrap -->
    <link href="%s" rel="stylesheet">
    <![endif]-->
    <style type="text/css">
        table tr td{
            vertical-align: middle;
        }
        .hidden-detail,.hidden-tr{
            display:none;
        }
        .result_red{
            background: red;
            color: white;
        }
        .result_green{
            background: green !important;
            color: white;
        }
    </style>
</head>
<body>
	''' % (titles, getRootPath() + '/files/plugs/bootstrap.min.css')
    return title

def testRegion(title):
    text = '''<div  class='col-md-12' style='margin-left:3%;'>'''
    text += '<h1>%s接口测试的结果</h1>' % title
    return text

def dataOutline(url, starttime, endtime, passge, fail):
    beijing = '''
    <table  class="table table-hover table-condensed">
            <tbody>
                <tr><td><strong>接口url:</strong> %s</td></tr>
                <tr><td><strong>开始时间:</strong> %s</td></tr>
                <tr><td><strong>结束时间:</strong> %s</td></tr>
                <tr><td><strong>耗时:</strong> %s</td></tr>
                <tr><td><strong>结果:</strong>
                        <span>成功: <strong >%s</strong>
                        失败:<strong >%s</strong>
                    </td>                  
			    </tr> 
			   </tbody></table>
			   </div> '''%(url, starttime, endtime, (endtime - starttime), passge, fail)
    return beijing

def createTableHeader(headItems):
    header = '''<div class="row " style="margin:30px">
                    <div>
                        <div class="btn-group" role="group" aria-label="...">
                            <button type="button" id="check-all" class="btn btn-primary">所有用例</button>
                            <button type="button" id="check-success" class="btn btn-success">成功用例</button>
                            <button type="button" id="check-failure" class="btn btn-danger">失败用例</button>
                        </div>
                    <div class="btn-group" role="group" aria-label="...">
                </div>'''
    header += '''<table class="table table-hover table-condensed table-bordered" style="word-wrap:break-word; word-break:break-all; margin-top: 7px; text-align: center;">'''
    for i in range(len(headItems)):
        header += '<td style="vertical-align: middle;"><strong>%s</strong></td>' % headItems[i]
    return header

def renderItem(item, showIds):
    listItem = item['listItem']
    isPass = '通过'
    resultClass = 'result_green'
    className = 'success'
    requestTime = item['result']['requestTime']
    # 删除不需要显示的key
    showItem = copy.deepcopy(item['result'])
    delItemList = ['requestTime', 'url']
    for i in range(len(delItemList)):
        if delItemList[i] in showItem:
            del showItem[delItemList[i]]

    if item['isPass'] == 1:
        isPass = '失败'
        resultClass = 'result_red'
        className = 'failure'
    trItem = '<tr class="case-tr %s">' % className
    for i in range(len(showIds)):
        trItem += '<td style="vertical-align: middle;">%s</td>' % listItem[showIds[i]]
    # 结果
    trItem += '<td style="vertical-align: middle;">%s</td>' % showItem
    trItem += '<td class="%s" style="vertical-align: middle;">%s</td>' % (resultClass, isPass)
    trItem += '<td style="vertical-align: middle;">%s</td>' % requestTime
    trItem += '</tr>'
    return trItem

htmlFooter = '''</div></div></table><script src="%s"></script>
<script src="%s"></script>
<script type="text/javascript">
    $("#check-all").click(function(e){
	    $(".case-tr").removeClass("hidden-tr");
	});
    $("#check-failure").click(function(e){
	    $(".case-tr").removeClass("hidden-tr");
        $(".success").addClass("hidden-tr");
        $(".failure").removeClass("hidden-tr");
	});
	$("#check-success").click(function(e){
        $(".case-tr").removeClass("hidden-tr");
        $(".success").removeClass("hidden-tr");
        $(".failure").addClass("hidden-tr");
	});
</script>
</body></html>''' % (getRootPath() + '/files/plugs/jquery-1.10.2.js', getRootPath() + '/files/plugs/bootstrap.min.js')

def outputFile(text, fileName):
    day = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
    basdir = getRootPath()
    filepath = os.path.join(basdir + '/files/report/%s-%s.html' % (day, fileName))
    # if os.path.exists(filepath) is False:
    #     os.system(r'touch %s' % filepath)
    # else:
    with open(filepath, 'wb') as f:
        f.write(text.encode('utf-8'))