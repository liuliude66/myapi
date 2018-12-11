#! python
# -*- coding:utf-8 -*-

from com.forum.lottery.api.LoginApi import LoginApi
from com.forum.lottery.api.CountdownApi import CountdownApi

if __name__ == '__main__':
    username = '1002'
    password = '123456'
    loginApiInstance = LoginApi(username, password)
    loginApiInstance.run()

    countdownInstance = CountdownApi()
    countdownInstance.run()
