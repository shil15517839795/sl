#!/usr/bin/python
# -*-coding:utf-8-*-
from appium import webdriver
from time import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import logging
import logging.config



logging.config.fileConfig(r'E:\shi\Python\ziDongHua\log\logging.conf')
logging.getLogger()#日志采集点

capability={
  "platformName": "Android",#连接设备的操作系统
  "platformVersion": "5.1.1",#连接设备操作系统的版本
  "deviceName": "127.0.0.1:62001",#连接设备的IP地址和端口号
  "noReset": False,#在当前session下不会重置应用的状态
  "appActivity": "com.tal.kaoyan.ui.activity.SplashActivity",#app的activity
  "appPackage": "com.tal.kaoyan"#app的包名
}
logging.info('start_app')
driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",capability)#启动app
driver.implicitly_wait(3)#隐式等待
logging.info('skip')
driver.find_element_by_id('com.tal.kaoyan:id/tv_skip').click()#根据id定位跳过并点击
logging.warning('agree')
driver.find_element_by_id('com.tal.kaoyan:id/tip_commit').click()#根据id定位同意并点击
# driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').send_keys('15517839795')#输入内容，是字符串类型
# driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext').send_keys('123456')#输入内容，是字符串类型
# driver.find_element_by_id('com.tal.kaoyan:id/login_login_btn').click()#点击登录