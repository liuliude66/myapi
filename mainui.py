#! python
# -*- coding:utf-8 -*-

from tkinter import *
from tkinter import ttk
import datetime
from com.forum.special.testCase.loginTest import LoginTest
from com.forum.special.testCase.betTest import BetTest
from com.forum.special.htmls.loginModuleHtml import *
import threading


class AppUI(object):
    path = ''

    def __init__(self):
        self.root = Tk()
        self.create_menu(self.root)
        self.root.title("API测试工具")
        self.root.update()

        self.label_log = ttk.Label(self.root, width=220, wraplength=220, foreground='green', background='grey',
                                   text='执行日志打印')
        self.label_log.pack()

        # 以下方法用来计算并设置窗体显示时，在屏幕中心居中
        cur_width = self.root.winfo_width()  # get current width
        cur_height = self.root.winfo_height()  # get current height
        scn_width, scn_height = self.root.maxsize()  # get screen width and height
        tmp_cnf = '550x350+%d+%d' % ((scn_width - cur_width) / 7, (scn_height - cur_height) / 4)
        self.root.geometry(tmp_cnf)
        self.root.mainloop()

    def create_menu(self, root):
        menu = Menu(root)
        # 创建二级菜单
        register_menu = Menu(menu, tearoff=0)
        register_menu.add_command(label="执行", command=self.register)
        register_menu.add_separator()

        login_menu = Menu(menu, tearoff=0)
        login_menu.add_command(label="执行", command=self.login)
        login_menu.add_separator()

        lottery_layout_menu = Menu(menu, tearoff=0)
        lottery_layout_menu.add_command(label="执行", command=self.lottery_layout)
        lottery_layout_menu.add_separator()

        lottery_bet_menu = Menu(menu, tearoff=0)
        lottery_bet_menu.add_command(label="执行", command=self.lottery_bet)
        lottery_bet_menu.add_separator()

        about_menu = Menu(menu, tearoff=0)
        about_menu.add_command(label="版本号：V1.0.0")

        # 在菜单栏中添加以下一级菜单
        menu.add_cascade(label="注册专项", menu=register_menu)
        menu.add_cascade(label="登录专项", menu=login_menu)
        menu.add_cascade(label="彩种布局", menu=lottery_layout_menu)
        menu.add_cascade(label="彩种投注", menu=lottery_bet_menu)
        menu.add_cascade(label="关于我们", menu=about_menu)

        root['menu'] = menu

    def register(self):
        self.create_log("注册开始执行...")
        exec_thread = threading.Thread(target=self.register_action)
        exec_thread.setDaemon(True)
        exec_thread.start()

    def login(self):
        self.create_log("登录开始执行...")
        exec_thread = threading.Thread(target=self.login_action)
        exec_thread.setDaemon(True)
        exec_thread.start()

    def lottery_layout(self):
        self.create_log("获取布局开始执行...")
        exec_thread = threading.Thread(target=self.lottery_layout_action)
        exec_thread.setDaemon(True)
        exec_thread.start()

    def lottery_bet(self):
        self.create_log('hello lottery_bet...')

    def create_log(self, content):
        message = self.label_log.cget("text")
        message += ("\n" + content)
        self.label_log.config(text=message)

    def register_action(self):
        try:
            start_time = datetime.datetime.now()
            # 注册专项
            result_dic = LoginTest().specialRegisteCase()
            end_time = datetime.datetime.now()
            handleRegisterHtmlData(start_time, end_time, result_dic)
            self.create_log("注册结束执行...")
        except Exception as ex:
            self.create_log("！！！！！！！！！注册执行异常！！！！！！！！！")
            self.create_log(str(ex.args))

    def login_action(self):
        try:
            start_time = datetime.datetime.now()
            result_dic = LoginTest().specialLoginCase()
            end_time = datetime.datetime.now()
            handleLoginHtmlData(start_time, end_time, result_dic)
            self.create_log("登录结束执行...")
        except Exception as ex:
            self.create_log("！！！！！！！！！登录执行异常！！！！！！！！！")
            self.create_log(str(ex.args))

    def lottery_layout_action(self):
        try:
            start_time = datetime.datetime.now()
            result_dic = BetTest().interfaceLotteryLayoutCase()
            end_time = datetime.datetime.now()
            print(result_dic)
            # handleLoginHtmlData(start_time, end_time, result_dic)
            self.create_log("获取布局结束执行...")
        except Exception as ex:
            self.create_log("！！！！！！！！！获取布局执行异常！！！！！！！！！")
            self.create_log(str(ex.args))

    def lottery_bet_action(self):
        try:
            start_time = datetime.datetime.now()
            result_dic = BetTest().interfaceBetCase()
            end_time = datetime.datetime.now()
            print(result_dic)
            # handleLoginHtmlData(start_time, end_time, result_dic)
            self.create_log("获取布局结束执行...")
        except Exception as ex:
            self.create_log("！！！！！！！！！获取布局执行异常！！！！！！！！！")
            self.create_log(str(ex.args))

if __name__ == "__main__":
    AppUI()
