#coding:utf-8
from json import loads
from tools.HttpConnector import HttpConnector

class APItest():
    def __init__(self,proxy_url=''):
        self.__protocol='http'
        self.__method='GET'
        self.__domain=''
        self.__uri=''
        self.__param={}
        self.__body=''
        self.__field=[]
        self.__header={}
        self.__h=HttpConnector(proxy_url) if proxy_url else HttpConnector()

    #设置协议：http or https
    def setProtocol(self, protocol='http'):
        self.__protocol = protocol

    #设置请求方法：get or post
    def setMethod(self, method='GET'):
        self.__method = method.upper()

    #设置域名 domain or host:port
    def setDomain(self, domain):
        self.__domain = domain

    #设置uri，斜划线开头，末尾不带问好
    def setUri(self, uri):
        self.__uri = uri

    #初始化param
    def initParam(self,param):
        if isinstance(param,dict):
            self.__param = param
        else:
            raise TypeError('param should be dict !!!')

    #设置param参数
    def setParam(self, pkey , pvalue):
        self.__param[pkey] = pvalue

    #设置post参数
    def setBody(self, body):
        self.__body = body

    #设置multipart参数,主要用于文件上传,现未增加此功能
    def setFiles(self, field):
        self.__field=field

    #初始化header
    def initHeader(self,header):
        if isinstance(header,dict):
            self.__header = header
        else:
            raise TypeError('header should be dict !!!')

    #设置header
    def setHeader(self, pkey, pvalue):
        self.__header[pkey] = pvalue

    #生成url
    def __makeUrl(self):
        if self.__param:
            from urllib.parse import urlencode
            url='%s://%s%s?%s'%(self.__protocol,self.__domain,self.__uri,urlencode(self.__param))
        else:
            url='%s://%s/%s'%(self.__protocol,self.__domain,self.__uri)
        return url

    #执行测试
    def run(self):
        try:
            url=self.__makeUrl()
            if self.__body:
                res=self.__h.conn(url=url,method=self.__method,body=self.__body,header=self.__header)
            else:
                res=self.__h.conn(url=url,method=self.__method,header=self.__header)
            return loads(res)
        except Exception as e:
            print(e)
            return 'err'

if __name__ == "__main__":
    from tools.ResultDecorator import decorator
    from urllib.parse import urlencode

    @decorator(SmokeTest=False)
    def test():
        test=APItest()
        param={
            'ch': 'AppStore',
            'fquc': '',
            'ios_ver': '10.3',
            'mid': 'test150996569523108190',
            'model': 'online_test',
            'sdk_ver': '1.0.5',
            'ss': '3',
            'tid': '',
            'vr': '3.6.0',
            'ver': '36000',
            'province': '北京市',
            'flag': '1'
        }
        expect_json={
            'error': 1,
            'msg': "ok1",
            'data': {}
        }
        test.setDomain('toffee.app.tvfanqie.com')
        test.setUri('/android/common/online')
        test.initParam(param)
        return expect_json,test.run()

    test()
    #print(test(func_data=True))

