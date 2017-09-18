#!/usr/bin/python3.5
#coding:utf-8
import os,sys,time
import unittest

thispath = os.path.abspath(os.path.dirname(sys.argv[0]))
basepath = thispath[:-5]
sys.path.append(basepath)

from conf.config import RUN_ALL_CASE,RUN_MODULES,RUN_CLASSES,RUN_CASES
from tools import HTMLTestRunner

#cases文件路径
path = os.path.abspath(os.path.dirname(sys.argv[0]))
cases_path= path.replace('main','cases')

if RUN_ALL_CASE:
    #全局运行case
    #将case目录下的所有case生成suits
    suits = unittest.TestLoader().discover(cases_path,pattern='case*.py')
else:
    #控制case范围
    files = os.listdir(cases_path)

    #模块过滤
    modules_files = ["cases."+i for i in files if (i[:4]=="case" and i in RUN_MODULES)]
    suit_list = []
    for md in modules_files:
        tmp=__import__(md,fromlist=('case',)).case
        cls_names=[cls for cls in dir(tmp) if cls[0:4]=="case" and cls in RUN_CLASSES]
        for name in cls_names:
            classes=getattr(tmp,name)
            #suit=unittest.TestLoader().loadTestsFromTestCase(classes)#根据类直接生成suit
            #case过滤
            case_names=[cn for cn in dir(classes) if (cn[0:4]=="test" and cn in RUN_CASES)]
            suit_list.append(unittest.TestSuite(map(classes, case_names)))

    suits= unittest.TestSuite(suit_list)

log_path=path.replace('main','log')
filename=log_path+r"/test_%d.html"%int(time.time())
fp=open(filename,'wb')
runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'自动化测试报告',description=u'自动化测试报告desc',verbosity=2)
runner.run(suits)
fp.close()

#发送结果邮件，代码后续补充
