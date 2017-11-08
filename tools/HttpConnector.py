#!/usr/bin/python3.5
#coding:utf-8
import urllib3,gzip,io
from urllib.parse import urlencode
from tools.Conf import Conf

class HttpConnector():
    def __init__(self,proxy_url=''):
        proxy=proxy_url if proxy_url else Conf().get_conf('config.PROXY_URL')
        if proxy:
            self.h=urllib3.ProxyManager(proxy)
        else:
            self.h=urllib3.PoolManager()

    #通过代理访问指定请求并返回请求结果
    def conn(self,url='',method='GET',body='',header={}):
        res=False
        if method.upper()=='GET':
            res=self.h.request(method='GET',url=url,headers=header)
        elif method.upper()=='POST':
            if body:
                res=self.h.request(method='POST',url=url,headers=header,body=body)
        return res.data.decode()

    #通过代理进行文件上传，并返回请求结果
    def file_poster(self,url='',fields=[],header={}):
        bfile,content_type=urllib3.encode_multipart_formdata(fields)
        header['Content-Type']=content_type

        res = self.h.request(method='POST',url=url,headers=header,body=bfile)
        #判断是否压缩报文
        if res.getheader('Content-Encoding','') == 'gzip':
            buf = io.StringIO(res.data)
            res=gzip.GzipFile(fileobj=buf)
            return res.read()
        else:
            return res.data.decode()


if __name__=="__main__":
    head={
        'Host': 'toffee.app.test.tvfanqie.com',
        'User-Agent': '360 Video App/2.1.0 Android/5.1 QIHU'
    }

    para={
        'uidshow':11543,
        'crumb':'a9e591',
        'vr':'2.7.0',
        'fquc':'',
        'mid':'f8f377c765b2615e3449f647fe09ab3b'
    }

    fields=[
        ('ch','gw'),
        ('crumb','7daae8'),
        ('fquc','bmlja25hbWU9JUU1JTg4JTk4JUU3JUE2JThGJUU1JThBJUE5JnNpZ249NThhNmEzMTk0ZjJhYTQyNjNjZjliMmM1YWY1YjliYzZ4aWFua2FudWN1aWQ9MjAwMDAwMDIyMjEmbG9naW5fdGltZT0xNTA1NzI0MzY4JnRodW1iPTFfdDAwZGY1NTFhNTgzYTg3ZjRlOSY='),
        ('thumb',('111.png',open('e:\\111.png','rb').read(),))
    ]
    url='http://toffee.app.test.tvfanqie.com/iphone/user/savethumb?'+urlencode(para)
    res = HttpConnector().file_poster(url,fields,head)
    print(res)