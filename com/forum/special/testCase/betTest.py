#! /usr/bin/python
# -*- coding:utf-8 -*-

import logger

from com.forum.special.service.betHttpTool import BetHttpTool
from com.forum.special.testCase.publicHandle import PublicHandle

# 投注模块测试
class BetTest(PublicHandle):
    def interfaceLotteryLayoutCase(self): # 彩种布局
        htmlList = []
        success1, result1 = BetHttpTool.postBetAllLottery()
        htmlList.append(self.showInterfaceDic(result1, '获取彩种列表：%s个' % len(result1['data'])))
        if success1 == 1:
            print('error')
        else:
            # 循环彩种
            lotteryList = result1['data']
            for i in range(len(lotteryList)):
                print('进入了%s - %s' % (i, len(lotteryList)))
                lotteryMes = lotteryList[i]
                lotteryId = lotteryMes['lotteryId']
                success2, result2 = BetHttpTool.postBetPlayGroupItems(lotteryId)
                htmlList.append(self.showInterfaceDic(result2, '%s - 彩种玩法列表' % lotteryMes['name']))
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
                            htmlList.append(self.showInterfaceDic(result3, '%s - %s - 玩法布局' % (lotteryMes['name'], playWayMes['name'])))
            return htmlList

    def interfaceBetCase(self):
        htmlList = []
        success1, result1 = BetHttpTool.postBetAllLottery()
        htmlList.append(self.showInterfaceDic(result1, '获取彩种列表'))
        if success1 == 1:
            print('error')
        else:
            # 循环彩种
            lotteryList = result1['data']
            for i in range(3):
                print('进入了%s' % i)
                lotteryMes = lotteryList[i]
                lotteryId = lotteryMes['lotteryId']
                success2, result2 = BetHttpTool.postBetPlayGroupItems(lotteryId)
                htmlList.append(self.showInterfaceDic(result2, '%s彩种玩法列表' % lotteryMes['name']))
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
                            htmlList.append(self.showInterfaceDic(result3, '%s玩法布局' % playWayMes['name']))
                            # if success3 == 1:
                            #     print('error')
                            # else:
                            #     success4, result4 = BetHttpTool.postBetBetting(None)
                            #     htmlList.append(self.showInterfaceDic(result4, '投注'))
                            #     if success4 == 1:
                            #         print('error')
                            #     else:
                            #         success5, result5 = BetHttpTool.postBetBettingNextPeriod(1)
                            #         htmlList.append(self.showInterfaceDic(result5, '自动续到下一期'))

            return htmlList

