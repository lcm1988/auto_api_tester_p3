#!/usr/bin/python3.5
#coding:utf-8

#只对比结构,不care数据
CMP_FRAME_ONLY=True

#debug模式，为真时打印对比结果
IS_DEBUG=True

#case运行范围配置
RUN_ALL_CASE=False#该配置项为false时RUN_MODULES，RUN_CLASSES，RUN_CASES生效
RUN_MODULES=['case_modle1','case_modle2']
RUN_CLASSES=['case_device1','case_device2']
RUN_CASES=['test_iphone_restart1','test_iphone_restart2']

#代理配置
PROXY_URL='http://192.168.52.1:8888/'

#邮箱配置
RECIEVER_LIST= ['516315002@qq.com','*****@163.com']
SMTP_SERVER='smtp.163.com'
EMAIL_NAME='*****@163.com'
EMAIL_PWD='******'

#数据库配置


#缓存配置
RDS_QA={
    'HOST':'11.212.4.111',
    'PORT':6342,
    'AUTH':'0fd24ec8238c1c2f'
}

#环境参数配置
COMMON_PARA={
    'ch':'',
    'ver':21000,    'vr':'2.1.0',
    'mid':'7dfe7793b85a93f0d7893cb0419102e9',
    'uidshow':'',
    'longitude':'116.490285',
    'latitude':'39.982712',
    'province':'北京市',
    'city':'北京市'
}
NT_HEADER={
    'Accept': 'text/html',
    'Host': 'toffee.app.test.tvfanqie.com',
    'Connection': 'Keep-Alive',
    'User-Agent': '360 Video App/2.1.0 Android/5.1 QIHU'
}
MSG_HEADER={
    'Accept': 'text/html',
    'Host': 'toffeemsg.app.test.tvfanqie.com',
    'Connection': 'Keep-Alive',
    'User-Agent': '360 Video App/2.1.0 Android/5.1 QIHU'
}
