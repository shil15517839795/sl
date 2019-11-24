#!/usr/bin/python
# -*-coding:utf-8-*-
import unittest

class Study_test(unittest.TestCase):

    @classmethod    #装饰符
    def setUpClass(cls):    #所有用例执行之前执行且只执行一次
        print('最开始执行的')
    @classmethod
    def tearDownClass(cls):     #所有用例执行之后执行且只执行一次
        print('最后执行的')

    def test01(self):
        print('执行了test01')

    def test02(self):
        print('执行了test02')

if __name__=='__main__':
    unittest.main()








# import unittest

# class Study_test(unittest.TestCase):
#
#     def setUp(self):    #每条用例执行前都执行一次
#         print('执行之前都要执行这个')
#     def tearDown(self):     #每条用例执行之后都执行一次
#         print('执行之后都要执行这个')
#
#     # @unittest.skip  #跳过执行test01
#     def test01(self):
#         print('执行了test01')
#
#     def test02(self):
#         print('执行了test02')
#
# if __name__=='__main__':
#     unittest.main()