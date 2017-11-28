#!/usr/bin/python3.5
#coding:utf-8
import os,sys,time
import unittest

thispath = os.path.abspath(os.path.dirname(sys.argv[0]))
#全局变量，项目根目录，绝对路径
BASE_PATH = thispath[:-5]
sys.path.append(BASE_PATH)

ENV='qa'
if ENV.lower()=='prod':
    from conf.prod import config
else:
    from conf.qa import config

from tools.ResultTdb import ResultTdb

def run(config):
    RUN_ALL_CASE=config.RUN_ALL_CASE
    RUN_MODULES=config.RUN_MODULES
    RUN_CLASSES=config.RUN_CLASSES
    RUN_CASES=config.RUN_CASES
    #cases文件路径
    cases_path= BASE_PATH+'/'+'cases'

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

    #jenkins对接，存储测试结果
    from tools.MyTestRunner import MyTestRunner
    result=MyTestRunner(verbosity=2).run(suits)
    runno=int(time.time())
    case_detail=[]
    for i in result:#每个文件一个list
        for s in i:#每个case一个list
            res={1:'fail',2:'err',0:'pass'}[s[0]] #测试结果
            (funcname,casepath)=str(s[1]).split(' ')
            apimsg=s[2] #case内置输出
            #print(apimsg)
            #分拆接口信息
            apiinfo=apimsg.strip().split('\n')
            cost,uri,tmp=0,'',[]
            for i in apiinfo:
                if i[:3]=='@地址':
                    uri=i[4:]#接口uri
                elif i[:3]=='@耗时':
                    cost=int(i[3:])#接口请求耗时
                else:
                    tmp.append(i)
            consoleinfo='\n'.join(tmp)#接口测试结果打印
            errmsg=s[3] #异常信息
            server=casepath[1:-1].split('.')[0][5:]
            case_detail.append([runno,'QA',funcname,casepath[1:-1],res,consoleinfo,errmsg,cost,uri,server])

    pass_cnt=len([1 for i in case_detail if i[4]=='pass'])
    fail_cnt=len([1 for i in case_detail if i[4]=='fail'])
    err_cnt=len([1 for i in case_detail if i[4]=='err'])
    print('成功数：%d'%pass_cnt,'失败数：%d'%fail_cnt,'异常数：%d'%err_cnt)

    from termcolor import cprint
    cprint('未成功case:','red',attrs=['bold','reverse'])
    res='\t%s'%('\n\t'.join([i[3]+'.'+i[2] for i in case_detail if i[4] in ('fail','err')]))
    cprint(res,'red',attrs=['bold','reverse'])
    #测试结果入库
    ResultTdb(config.REPORT_DB).saveres(case_detail)


if __name__=="__main__":
    run(config)



