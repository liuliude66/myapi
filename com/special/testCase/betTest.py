#! /usr/bin/python
# -*- coding:utf-8 -*-

import json, datetime

from com.special.service.betHttpTool import BetHttpTool
from com.special.testCase.publicHandle import PublicHandle
from com.tool.transTool import TransTool
from com.tool.testConfig import TestConfig
from com.special.htmls.interfaceHtml import handleInterfaceData

# 投注模块测试
class BetTest(PublicHandle):
    def interfaceLotteryLayoutCase(self, betLotteryName): # 彩种布局
        starttime = datetime.datetime.now()
        success1, result1 = BetHttpTool.postBetAllLottery()
        # htmlList.append(self.showInterfaceDic(result1, '获取彩种列表：%s个' % len(result1['data'])))
        if success1 == 1:
            print('error')
        else:
            # 循环彩种
            lotteryList = result1['data']
            for i in range(len(lotteryList)):
                lotteryMes = lotteryList[i]
                if lotteryMes['name'] == betLotteryName:
                    lotteryHtmlList = []
                    lotteryId = lotteryMes['lotteryId']
                    success2, result2 = BetHttpTool.postBetPlayGroupItems(lotteryId)
                    lotteryHtmlList.append(self.showInterfaceDic(result2, '%s - 彩种玩法列表: %s个' % (lotteryMes['name'], len(result2['data']))))
                    if success2 == 1:
                        print('error')
                    else:
                        playList = result2['data']
                        for j in range(len(playList)):
                            playWayList = playList[j]['playWayData']
                            for k in range(len(playWayList)):
                                playWayMes = playWayList[k]
                                playId = playWayMes['playId']
                                success3, result3 = BetHttpTool.postBetGetLayoutItem(playId)
                                lotteryHtmlList.append(self.showInterfaceDic(result3, '%s - %s - 玩法布局' % (lotteryMes['name'], playWayMes['name'])))
            endtime = datetime.datetime.now()
            handleInterfaceData(starttime, endtime, lotteryHtmlList, TestConfig().getNormalInterfaceData(betLotteryName + '玩法布局'))
            return

    def getLotteryCategory(self, lotteryClassName):
        category = ''
        if lotteryClassName.endswith('QuickThree'):
            category = '快三'
        elif lotteryClassName.endswith('ElevenPickFive'):
            category = '11选5'
        elif lotteryClassName.endswith('ArrangeThree'):
            category = '排列三'
        elif lotteryClassName.endswith('ThreeD'):
            category = '福彩3d'
        elif lotteryClassName.endswith('FrequentHappy'):
            category = '时时乐'
        elif lotteryClassName.endswith('PK10'):
            category = 'PK10'
        elif lotteryClassName.endswith('FrequentLottery'):
            category = '时时彩'
        elif lotteryClassName.endswith('PCEggs'):
            category = 'PC蛋蛋'
        elif lotteryClassName.endswith('28'):
            category = '幸运28'
        elif lotteryClassName.endswith('SixMark'):
            category = '六合彩'
        return category;

    def interfaceBetCase(self, loginDic, betLotteryName): # 指定彩种输出
        success1, result1 = BetHttpTool.postBetAllLottery()
        if success1 == 1:
            print('error')
        else:
            lotteryList = result1['data']
            for i in range(len(lotteryList)):
                lotteryMes = lotteryList[i]
                if betLotteryName == lotteryMes['name']:
                    starttime = datetime.datetime.now()
                    lotteryHtmlList = []
                    print('进入了%s - %s' % (i, len(lotteryList)))
                    lotteryId = lotteryMes['lotteryId']
                    success2, result2 = BetHttpTool.postBetPlayGroupItems(lotteryId)
                    # lotteryHtmlList.append(self.showInterfaceDic(result1, '获取彩种列表'))
                    lotteryHtmlList.append(self.showInterfaceDic(result2, '%s彩种玩法列表' % lotteryMes['name']))
                    if success2 == 1:
                        print('error')
                    else:
                        playList = result2['data']
                        for j in range(len(playList)):
                            playWayList = playList[j]['playWayData']
                            for k in range(len(playWayList)):
                                print('进入了子玩法%s - %s' % (k, len(playWayList)))
                                playWayMes = playWayList[k]
                                playId = playWayMes['playId']
                                success3, result3 = BetHttpTool.postBetGetLayoutItem(playId)
                                lotteryHtmlList.append(self.showInterfaceDic(result3, '%s玩法布局' % playWayMes['name']))
                                if success3 == 1:
                                    print('error')
                                else:
                                    configDic = TestConfig.getBetContentData(lotteryMes['name'], self.getLotteryCategory(lotteryMes['lotteryClassName']))
                                    listItem = TransTool().TransSpecial(configDic)
                                    for m in range(len(listItem)):
                                        show = listItem[m]
                                        betItem = dict()
                                        betItem['rebate'] = 0
                                        betItem['playId'] = playId
                                        if isinstance(show['money'], int):
                                            betItem['unitFee'] = 100 * int(show['money'])
                                        else:
                                            betItem['unitFee'] = show['money']
                                        betItem['issue'] = lotteryMes['currentIssue']
                                        betItem['numbers'] = show['numbers']
                                        betList = [betItem]
                                        jsonStr = json.dumps(betList)
                                        success4, result4 = BetHttpTool.postBetBetting(jsonStr)
                                        lotteryHtmlList.append(self.showInterfaceDic(result4, '投注'))
                    endtime = datetime.datetime.now()
                    handleInterfaceData(starttime, endtime, loginDic + lotteryHtmlList, TestConfig().getBetInterfaceData(lotteryMes['name'] + '投注'))
            return