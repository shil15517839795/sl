#!/usr/bin/python
#-*- conding:utf-8 -*-
# from   selenium  import  webdriver
# from   time    import  sleep
# QQ = webdriver.Chrome()
# QQ.get('http://qzone.qq.com/')
# sleep(3)
# QQ.switch_to_frame('login_frame')
# sleep(3)
# QQ.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
# sleep(3)
# QQ.find_element_by_xpath('//*[@id="u"]').send_keys('2446607275')
# sleep(3)
# QQ.find_element_by_xpath('//*[@id="p"]').send_keys('xinghaoyouni275')
# sleep(3)
# QQ.find_element_by_xpath('//*[@id="login_button"]').click()
# sleep(3)
# QQ.find_element_by_xpath('//*[@id="$1_substitutor_content"]').send_keys('宁愿修炼不完美的自己，也不愿期待找到一个完美的别人')
# sleep(5)
# QQ.find_element_by_xpath('//*[@id="QM_Mood_Poster_Inner"]/div/div[4]/div[4]/a[2]/span').click()

# from  selenium   import webdriver
# from  time   import   sleep
# dr = webdriver.Chrome()
# dr.get('http://www.baidu.com')
# sleep(3)
# dr.find_element_by_xpath('//*[@id="kw"]').send_keys('boss直聘')
# sleep(3)
# dr.find_element_by_xpath('//*[@id="su"]').click()
# dr.find_element_by_xpath('//*[@id="4001"]/div[1]/h3/a[1]').click()


#web自动化
#selenium:是自动化测试的工具集
#selenium 1.0 的组成  2.0和3.0没有太大的区别
#1，selenium IDE  是火狐浏览器的插件，作用：是录制和回放
#2，selenium Grid 是自动化测试的一个辅助工具，作用：可以实现在不同的环境中同时执行测试
#3，selenium RC 是自动化测试的核心（1.0），作用：控制浏览器的行为

#selenium2.0 的组成
#selenium1.0（selenium IDe/grid /rc) + webdriver:是selenium2.0的核心，主要作用和rc相同
# 作用：控制浏览器的行为

#RC:通过将测试代码转换成JAVAScript能够识别的动作从而间接的控制浏览器

#webdriver：通过将浏览器的所有的原生接口集成到webdriver驱动中，然后通过驱动直接控制浏览器

# from selenium import webdriver
# from time import sleep
# dr = webdriver.Chrome()
# dr.get('https://qzone.qq.com/')
# sleep(2)
# dr.switch_to.frame('login_frame')
# sleep(2)
# dr.find_element_by_id('switcher_plogin').click()
# sleep(3)
# dr.find_element_by_id('u').send_keys('2446607275')
# dr.find_element_by_id('p').send_keys('xinghaoyouni275')
# dr.find_element_by_class_name('btn').click()
# sleep(3)

#selenium 环境搭建与安装

#定位一组对象

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains  #动作链

# dr = webdriver.Chrome()
# dr.get('https://qzone.qq.com/')
# sleep(2)
# dr.switch_to.frame('login_frame')     #iframe 内嵌框架 切换到某个框架上去（通过id，name的值）
# dr.switch_to.default_content('')   #能够回退到上一个框架外
# dr.switch_to.parent_frame()   #回退到最初的页面
# sleep(2)
# dr.find_element_by_id('switcher_plogin').click()
# sleep(3)
# dr.find_element_by_id('u').send_keys('24466072')
# dr.find_element_by_id('p').send_keys('xinghaoyouni275')

# sleep(3)
# dr.find_element_by_xpath('//*[@id="login_button"]').click()
# dr.switch_to.frame('tcaptcha_iframe')
# wd = dr.find_element_by_xpath('//*[@id="tcaptcha_drag_button"]')
# sleep(4)
#drag_and_drop两个参数（起始位置，结束位置）\
#drag_and_drop_by_offset三个参数（起始位置，x轴坐标，和y轴坐标）
# ActionChains().drag_and_drop_by_offset(wd,195,0).perform()


# ww = dr.find_elements_by_class_name('mnav')  #定位一组对象，找到相同的元素

# for i in ww:
#     b = i.get_attribute('href')         #获取某个属性的值    href获取网址   text 获取文本
#     print(b)
#层级定位  先定位一个大的区域，再从大的区域中找
#定位先定位父元素必须事唯一的，在定位子元素可以有多个
#模拟鼠标移动
# tt = dr.find_element_by_id('J_roomCountList').find_elements_by_tag_name('option')

# print(len(tt))
# for i in tt:
#     if i == 7:
#         break
#     else:
#         i.click()   #获取某个属性
#         sleep(2)

# jd = dr.find_element_by_xpath('//*[@id="J_cate"]/ul').find_elements_by_class_name('cate_menu_lk')
# print(len(jd))
#
# for i in jd:
#     jj = ActionChains(dr).move_to_element(i).perform()
#     sleep(3)
#     print(jj)


#任何浏览器管理窗口的原理
#将每一个窗口用一个特定的字符来标识,句柄
#只需要获取到每一个窗口的标识号，通过切换标识号，就能达到切换窗口的目的
from selenium import webdriver
from time import sleep
import selenium.webdriver.support.ui as ui        #导入模块   智能等待
from selenium.webdriver.common.action_chains import ActionChains  #动作链

# dr = webdriver.Chrome()
# dr.get('https://www.baidu.com')
# # sleep(3)     #强制等待
# #创建一个智能等待
# unit = ui.WebDriverWait(dr,10)     #创建一个智能等待   10事最大等待时间
# #如果一个元素出现了就不必在等待  如hao123
# unit.until(lambda dr:dr.find_element_by_link_text('hao123').is_displayed())
# #检查hao123文本是否出现，如果出现执行下面的代码，如果没出现一直等待，最大等待10秒
#
# dr.find_element_by_link_text('新闻').click()








# sleep(2)
# for i in range(0,10000,500):
#     js = 'var q=document.documentElement.scrollTop={}'.format(i) #拖动滚动条的语句
#
#     dr.execute_script(js)  #执行鼠标拖动滚动跳的函数
#     sleep(2)
#
# dr.find_element_by_xpath('/html/body/input').click()
# sleep(2)
# #切换到弹出框上去
# ww = dr.switch_to_alert()
# #获取弹出框上面的文本
# print(ww.text)
# #点击确定
# ww.accept()
# #点击取消
# ww.dismiss()
# #向弹出框输入数据
# ww.send_keys('dhjfruiwghfruyhgfu')


#获取当前窗口的标识
# print(dr.current_window_handle)
# dr.find_element_by_xpath('//*[@id="anony-nav"]/div[1]/ul/li[1]/a').click()
# sleep(2)
# aa = dr.window_handles
#
# #切换窗口
# dr.switch_to.window(aa[0])
# print(dr.title)

#Javascript： 动态网页





