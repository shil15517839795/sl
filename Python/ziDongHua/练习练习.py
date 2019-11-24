#!/usr/bin/python
# -*-coding:utf-8-*-
from appium import webdriver
from time import *
from selenium.webdriver.support.ui import WebDriverWait
capability={
  "platformName": "Android",
  "platformVersion": "5.1.1",
  "deviceName": "127.0.0.1:62001",
  "noReset": False,
  "appActivity": "com.tal.kaoyan.ui.activity.SplashActivity",
  "appPackage": "com.tal.kaoyan"
}
driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",capability)

WebDriverWait(driver,20).until(lambda x: x.find_element_by_id('com.tal.kaoyan:id/tv_skip')).click()
WebDriverWait(driver,100).until(lambda x: x.find_element_by_id('com.tal.kaoyan:id/tip_commit')).click()
# driver.find_element_by_id('com.tal.kaoyan:id/tv_skip').click()
# driver.find_element_by_id('com.tal.kaoyan:id/tip_commit').click()


















