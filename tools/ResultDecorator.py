#!/usr/bin/python3.5
#coding:utf-8
from tools.JsonCompare import JsonCompare

def APIdecorator(SmokeTest=False):
    def getfunc(func):
        def runtest(*args,**kwargs):
            expect_data,req_res= func(*args)
            if kwargs.get('func_data',False)==True:return req_res#检测func_data=True时只返回接口数据

            #print(dir(func))
            #后期可以根据以下两个参数拿到配置好的借口预期返回值，case可以只配置apitest类的参数和调用
            #print(func.__name__)#方法名
            #print(func.__module__)#方法所在文件名

            cmp_res=JsonCompare(expect_data,req_res,is_debug=False)
            comment=func.__doc__ if func.__doc__ else func.__name__
            print('%s RESULT OF "%s" %s'%('#'*10,comment,'#'*10))
            if SmokeTest:
                print('执行冒烟测试。。。')
                for i in cmp_res.frame_cmpare_result:print(i)#打印结构异常
                assert len(cmp_res.frame_cmpare_result)==0
            else:
                print('执行全数据比对。。。')
                for i in cmp_res.data_compare_result:print(i)#打印数据异常
                for i in cmp_res.frame_cmpare_result:print(i)#打印结构异常
                assert len(cmp_res.frame_cmpare_result)==len(cmp_res.data_compare_result)==0
            print('对比成功')
        return runtest
    return getfunc

@APIdecorator(1)
def myfunc():
    return 1,1

if __name__=="__main__":
    print(myfunc(func_data=True))#返回原方法结果
    myfunc()

