#!/usr/bin/python
# -*-coding:utf-8-*-

#调用手机的公告部分
from appium import webdriver
from time import *
# from selenium.common.exceptions import NoSuchElementException

#调用
capability={
  "platformName": "Android",#连接设备的操作系统
  "platformVersion": "5.1.1",#连接设备操作系统的版本
  "deviceName": "127.0.0.1:62001",#连接设备的IP地址和端口号
  "noReset": False,#在当前session下不会重置应用的状态
  "appActivity": "com.tal.kaoyan.ui.activity.SplashActivity",#app的activity
  "appPackage": "com.tal.kaoyan"#app的包名
}
driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",capability)#启动app
driver.implicitly_wait(3)#隐式等待
driver.find_element_by_id('com.tal.kaoyan:id/tv_skip').click()#根据id定位跳过并点击
driver.find_element_by_id('com.tal.kaoyan:id/tip_commit').click()#根据id定位同意并点击
# def test_01():#测试输入账号
#     driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').send_keys('15517839795')#输入内容，是字符串类型
# test_01()
# def test_02():#测试输入密码
#     driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext').send_keys('123456')#输入内容，是字符串类型
# test_02()
# driver.find_element_by_id('com.tal.kaoyan:id/login_login_btn').click()#点击登录
# # # driver.close()














































# def haha():
#     try:
#         skip=driver.find_element_by_id('com.tal.kaoyan:id/tv_skip')#根据id定位跳过步骤
#     except NoSuchElementException:
#         print("no skip")
#     else:
#         skip.click()
# haha()
# def en():
#     try:
#         agree=driver.find_element_by_id('com.tal.kaoyan:id/tip_commit')#根据id定位同意
#     except NoSuchElementException:
#         print("no agree")
#     else:
#         agree.click()
# en()