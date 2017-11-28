#!/usr/bin/python3.5
#coding:utf-8
from tools.JsonCompare import JsonCompare
from tools.ExpectJson import Get_Expect

def APIdecorator(SmokeTest):
    def getfunc(fun):
        def runtest(*args,**kwargs):
            req_res = fun(*args)
            if kwargs.get('func_data',False)==True:return req_res#检测func_data=True时只返回接口数据

            #fun.__module__: 函数所在类; fun.__name__: 函数所在类; fun.__doc__: 函数说明;
            comment=fun.__doc__ if fun.__doc__ else fun.__name__

            #增加接口调试判断，调试情况下req_res会获取到两个值
            if isinstance(req_res,tuple) and len(req_res)==2:
                expect_json,req_res=req_res[0],req_res[1]
            else:
                expect_json=Get_Expect(fun.__module__,fun.__name__).expect_json

            if req_res=='request or jsonencode err':
                print('接口数据获取异常')
                raise ConnectionError('未得到预期格式结果')

            print('%s RESULT OF "%s" %s'%('#'*10,comment,'#'*10))
            cmp_res=JsonCompare(expect_json,req_res,is_debug=False)
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
    return 1,2

if __name__=="__main__":
    myfunc()
    print(myfunc(func_data=True))#返回原方法结果
    a=myfunc(func_data=True)
    b,a=a[0],a[1]
    print(b,a)
