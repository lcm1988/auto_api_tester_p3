#!/usr/bin/python3.5
#coding:utf-8
import time
import unittest
from conf import config
from tools.ResultDecorator import decorator
from tools.APItest import APItest

class case_device1(unittest.TestCase):
    #定义初始数据方法
    def setUp(self):
        self.commonpara= config.COMMON_PARA.copy()
        #定义请求头
        self.headers= config.NT_HEADER.copy()
        self.start_time=time.time()

    #收尾方法，统计接口耗时
    def tearDown(self):
        self.end_time=time.time()
        print('@耗时%d'%int((self.end_time-self.start_time)*1000))

    @decorator(SmokeTest=True)
    def test_iphone_restart1(self):
        '''@NTAPI-程序后台唤起1'''
        para=self.commonpara.copy()
        request=APItest()
        request.setDomain('toffee.app.test.tvfanqie.com')
        request.setUri('/iphone/common/online')
        request.initHeader(self.headers)
        request.initParam(para)
        request.setParam('flag',2)
        expect_json={
            "error": 0,
            "msg": "ok1",
            "data": {}
        }
        return expect_json,request.run()

    @decorator(SmokeTest=False)
    def test_iphone_restart2(self):
        '''@NTAPI-程序后台唤起2'''
        para=self.commonpara.copy()
        request=APItest()
        request.setDomain('toffee.app.test.tvfanqie.com')
        request.setUri('/iphone/common/online')
        request.initHeader(self.headers)
        request.initParam(para)
        request.setParam('flag',2)

        #引用其他case的接口返回数据
        expect_json=self.test_iphone_restart1(func_data=True)

        return expect_json,request.run()

if __name__=="__main__":
    unittest.main()