#!/usr/bin/python
# -*-coding:utf-8-*-
from lei.aa import driver#从lei目录下导入aa.py文件
# from time import *
def login():
    driver.find_element_by_class_name('android.widget.TextView').click()    #点击注册
def picture():
    driver.find_element_by_id('com.tal.kaoyan:id/activity_register_userheader').click()     #点击添加头像
def check():
    aaa=driver.find_elements_by_id('com.tal.kaoyan:id/check')
    aaa[0].click()      #选择照片
    driver.find_element_by_id('com.tal.kaoyan:id/picture_tv_ok').click()     #点击确定
    driver.find_element_by_id('com.tal.kaoyan:id/menu_crop').click()     #点击右上角的对号确定
def username():
    driver.find_element_by_id('com.tal.kaoyan:id/activity_register_username_edittext').send_keys('shi123456') #输入账号
def password():
    driver.find_element_by_id('com.tal.kaoyan:id/activity_register_password_edittext').send_keys('s123123') #输入密码
def mail():
    driver.find_element_by_id('com.tal.kaoyan:id/activity_register_email_edittext').send_keys('1583792786@qq.com')#输入邮箱
def register():
    driver.find_element_by_id('com.tal.kaoyan:id/activity_register_register_btn').click()#点击立即注册
login()#点击注册
picture()#进入相册
check()#选择照片
username()#输入用户名
password()#输入密码
mail()#输入邮箱
register()#点击立即注册