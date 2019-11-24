#!/usr/bin/python
# -*-coding:utf-8-*-
import yaml
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
with open(r'E:\shi\Python\ziDongHua\config\head.yaml','r') as file:
    data=yaml.load(file,Loader=yaml.FullLoader)
print(data)
file.close()
capability={"platformName":data['platformName'],
            'platformVersion':data['platformVersion'],
            'deviceName':data['deviceName'],
            'noReset':data['noReset'],
            'appActivity':data['appActivity'],
            'appPackage':data['appPackage'],
            'ip':data['ip'],
            'port':data['port']
}
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',capability)
driver.find_element_by_id('com.tal.kaoyan:id/tv_skip').click()
driver.find_element_by_id('com.tal.kaoyan:id/tip_commit').click()
driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').send_keys('fafnkfa')
driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext').send_keys('123456')
driver.find_element_by_id('com.tal.kaoyan:id/login_login_btn').click()
