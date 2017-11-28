#!/usr/bin/python3.5
#coding:utf-8
import time
import unittest
from tools.ResultDecorator import APIdecorator
from tools.APItest import APItest
from tools.Conf import Conf

class case_device1(unittest.TestCase):
    #定义初始数据方法
    def setUp(self):
        self.commonpara = Conf().get_conf('config.COMMON_PARA').copy()
        # 定义请求头
        self.headers = Conf().get_conf('config.NT_HEADER').copy()
        self.start_time=time.time()

    #收尾方法，统计接口耗时
    def tearDown(self):
        self.end_time=time.time()
        print('@耗时%d'%int((self.end_time-self.start_time)*1000))

    @APIdecorator(SmokeTest=False)
    def test_iphone_restart1(self):
        '''@NTAPI-程序后台唤起1'''
        para=self.commonpara.copy()
        request=APItest()
        request.setDomain('toffee.app.tvfanqie.com')
        request.setUri('/iphone/common/online')
        request.initHeader(self.headers)
        request.initParam(para)
        request.setParam('flag',2)
        return request.run()


if __name__=="__main__":
    unittest.main()