#!/usr/bin/python3.5
#coding:utf-8

#只对比结构,不care数据
CMP_FRAME_ONLY=True

#debug模式，为真时打印对比结果
IS_DEBUG=True

#case运行范围配置
RUN_ALL_CASE=False#该配置项为false时RUN_MODULES，RUN_CLASSES，RUN_CASES生效
RUN_MODULES=['case_modle']
RUN_CLASSES=['case_device']
RUN_CASES=['test_iphone_restart1','test_iphone_restart2']

#代理配置
USE_PROXY=True
PROXY_HOST='192.168.52.1'
PROXY_PORT=8888

#邮箱配置
RECIEVER_LIST= ['516315002@qq.com','*****@163.com']
SMTP_SERVER='smtp.163.com'
EMAIL_NAME='*****@163.com'
EMAIL_PWD='******'

#数据库配置


#缓存配置
RDS_QA={
    'HOST':'10.202.4.251',
    'PORT':6342,
    'AUTH':'0fd24ec8238c1c2f'
}


#环境参数配置

