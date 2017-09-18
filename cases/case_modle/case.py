#!/usr/bin/python3.5
#coding:utf-8

import unittest
from json import loads
from urllib.parse import urlencode
from conf import basedata
from tools.ResultDecorator import decorator
from tools.HttpConnector import HttpConnector

class case_device(unittest.TestCase):
    #定义初始数据方法
    def setUp(self):
        self.commonpara= basedata.commonpara.copy()
        #定义请求头
        self.headers= basedata.nt_headers.copy()

    def tearDown(self):
        pass

    @decorator
    def test_iphone_restart1(self):
        '''程序后台唤起1'''
        para=self.commonpara.copy()
        para['flag']=2
        url='http://toffee.app.test.tvfanqie.com/iphone/common/online?%s'%urlencode(para)
        res=HttpConnector().conn(url,'GET',header=self.headers)
        expect_json={
            "error": 0,
            "msg": "ok",
            "data": []
        }
        return expect_json,loads(res)

    @decorator
    def test_iphone_restart2(self):
        '''程序后台唤起2'''
        b=self.test_iphone_restart1(func_data=True)[1]
        expect_json={
            "error": 0,
            "msg": "ok",
            "data": {}
        }
        return expect_json,b

if __name__=="__main__":
    unittest.main()