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
    files = os.listdir(cases_path)#获取cases目录下各个项目文件夹

    #case开头的文件夹会被识别为项目文件夹，然后根据配置中需要运行的项目名称过滤
    project_modules = ["cases."+i for i in files if (i[:4]=="case" and i in RUN_MODULES)]

    suit_list = []
    for project_module in project_modules:
        #拼装项目目录
        project_module_path=cases_path+'/'+project_module.split('.')[1]

        #获取项目目录下的case文件名
        project_case_files=os.listdir(project_module_path)
        project_cases=[i.split('.')[0] for i in project_case_files if i[:4]=="case"]

        #等同于 from case import case_modle
        case_module=__import__(project_module,fromlist=project_cases)

        for i in project_cases:
            #获取case_modle下层各个case对象
            tmp=getattr(case_module,i)

            #获取文件中的类名，case开头的类会被识别，然后根据配置中需要运行的class名称过滤
            cls_names=[cls for cls in dir(tmp) if cls[:4]=="case" and cls in RUN_CLASSES]
            for name in cls_names:
                #根据case对象和类名获得类对象
                classes=getattr(tmp,name)

                #根据类直接生成suit
                #suit=unittest.TestLoader().loadTestsFromTestCase(classes)

                #获取类中的方法名，以test开头的方法会被识别，然后根据配置中需要运行的case名称过滤
                case_names=[cn for cn in dir(classes) if (cn[0:4]=="test" and cn in RUN_CASES)]

                #根据类名，方法名装载到suit中
                suit_list.append(unittest.TestSuite(map(classes, case_names)))
    #print(suit_list)#<cases.case_modle.case.case_device testMethod=test_iphone_restart1>
    suits= unittest.TestSuite(suit_list)

log_path=path.replace('main','log')
filename=log_path+r"/test_%d.html"%int(time.time())
fp=open(filename,'wb')
runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'自动化测试报告',description=u'自动化测试报告desc',verbosity=2)
runner.run(suits)
fp.close()

#发送结果邮件，代码后续补充
