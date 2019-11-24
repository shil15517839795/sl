#!/usr/bin/python
# -*-coding:utf-8-*-
import unittest
from App.test_run.HTMLTestRunner import HTMLTestRunner
import time
import os

case_path=r'E:\shi\Python\App\test_run' #测试用例的路径
discover=unittest.defaultTestLoader.discover(case_path,pattern='run*.py')  #discover测试集，匹配在case_path路径下的以run开头的脚本
if __name__ == '__main__':
    now=time.strftime('%Y %m %d %H %M %S')  #获取现在的时间
    report=r'E:\shi\Python\App\Report'  #存放报告的路径
    report_name=os.path.join(report,'%s.html' %(now))   #报告的名字
    with open(report_name,'wb') as file:
        runner=HTMLTestRunner(stream=file,
                              title=u'测试报告',
                              description=u'用例执行情况如下：',
                              tester=u'时雷',
                              verbosity=2   #0测试报告没有内容，1代表产生报告不详细，2表示产生的报告最详细
                              )
        run=HTMLTestRunner()
        runner.run(discover)