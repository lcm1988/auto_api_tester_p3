#!/usr/bin/python3.5
#coding:utf-8

class Get_Expect():
    def __init__(self,mdname,funcname):
        self.func=funcname
        self.fmd='expects.%s'%mdname

    @property
    def expect_json(self):
        tmp=__import__(self.fmd,fromlist=(self.fmd.split('.')[1],))
        if self.func in dir(tmp):
            data=getattr(tmp,self.func)
            return data
        else:
            raise AttributeError('未找到该方法的预期数据，请检查是否维护了case预期')

if __name__=="__main__":
    print(Get_Expect('case_HJ_API.case_blacklist','test_android_blacklist_add').expect_json)