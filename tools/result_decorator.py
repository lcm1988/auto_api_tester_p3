#!/usr/bin/python3.5
#coding:utf-8
from conf.config import CMP_FRAME_ONLY
from tools.json_compare import jsoncompare

def decorator(fun):
    def test(*args,**kwargs):
        comment=fun.__doc__ if fun.__doc__ else fun.__name__
        if kwargs.get('func_data',False)==True:return fun(*args)
        print("%s RESULT OF \"%s\" %s"%("#"*10,comment,"#"*10))
        a,b= fun(*args)
        res=jsoncompare(a,b)
        if res.frame_cmpare_result or res.data_compare_result:
            assert len(res.frame_cmpare_result)==0
            if not CMP_FRAME_ONLY:
                assert len(res.data_compare_result)==0
        else:
            print('对比成功')

    return test

@decorator
def myfunc():
    return 1,1

if __name__=="__main__":
    myfunc()#case调用，无返回结果
    print(myfunc(func_data=True))#返回原方法结果

