#!/usr/bin/python3.5
#coding:utf-8
from tools.JsonCompare import JsonCompare

def decorator(SmokeTest):
    def getfunc(fun):
        def runtest(*args,**kwargs):
            expect_data,req_res= fun(*args)
            if kwargs.get('func_data',False)==True:return req_res#检测func_data=True时只返回接口数据

            cmp_res=JsonCompare(expect_data,req_res,is_debug=False)
            comment=fun.__doc__ if fun.__doc__ else fun.__name__
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

@decorator(1)
def myfunc():
    return 1,1

if __name__=="__main__":
    print(myfunc(func_data=True))#返回原方法结果

