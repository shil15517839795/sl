#!/usr/bin/python
# -*-coding:utf-8-*
from appium import webdriver
from time import *
from selenium.webdriver.support.ui import WebDriverWait
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
driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').send_keys('wifhsodfha')#输入账号，是字符串类型
# driver.get_screenshot_as_file('../lei/s.png')#截图，保存到指定路径
# driver.save_screenshot('a.png')#截图
driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext').send_keys('123456')#输入密码，是字符串类型
# driver.get_screenshot_as_file('../lei/l.png')#截图，保存到指定路径
# driver.save_screenshot('b.png')#截图
driver.find_element_by_id('com.tal.kaoyan:id/login_login_btn').click()#点击登录
#
error_message = "账号不存在"
message = '//*[@text="{}"]'.format(error_message)
toast_element = WebDriverWait(driver,5).until(lambda x:x.find_element_by_xpath(message))
print(toast_element.text)
