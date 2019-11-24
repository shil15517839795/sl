#!/usr/bin/python
# -*-coding:utf-8-*-
import unittest

class Study_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('来日方长')

    @classmethod
    def tearDownClass(cls):
        print('傻逼傻逼')

    def test01(self):
        print('I hope you are here for me')

    def test02(self):
        print('I want time to be very simply')

    def test03(self):
        print('Light still')

    def test04(self):
        print('You still')

if __name__ == '__main__':
    unittest.main()