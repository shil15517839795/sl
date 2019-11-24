#!/usr/bin/python
# -*-coding:utf-8-*-
import unittest

class Study_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('时雷最帅')
    @classmethod
    def tearDownClass(cls):
        print('哈哈哈哈哈')

    def test01(self):
        print('You know what？')

    def test02(self):
        print('When I first saw you')

    def test03(self):
        print('I said to myself')

    def test04(self):
        print('Oh,my god!')

    def test05(self):
        print('This one is going to heart!')

if __name__=='__main__':
    unittest.main()
