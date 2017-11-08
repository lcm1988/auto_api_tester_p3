#!/usr/bin/python3.5
#coding:utf-8
from tools.JsonCompare import JsonCompare

def decorator(SmokeTest):
    def getfunc(fun):
        def runtest(*args,**kwargs):
            comment=fun.__doc__ if fun.__doc__ else fun.__name__
            if kwargs.get('func_data',False)==True:return fun(*args)
            print('%s RESULT OF "%s" %s'%('#'*10,comment,'#'*10))
            a,b= fun(*args)
            res=JsonCompare(a,b)
            if SmokeTest:
                print('执行冒烟测试。。。')
                assert len(res.frame_cmpare_result)==0
            else:
                print('执行全数据比对。。。')
                assert len(res.frame_cmpare_result)==len(res.data_compare_result)==0
            print('对比成功')
        return runtest
    return getfunc

@decorator(1)
def myfunc():
    return 1,1

if __name__=="__main__":
    myfunc()#case调用，无返回结果
    print(myfunc(func_data=True))#返回原方法结果

