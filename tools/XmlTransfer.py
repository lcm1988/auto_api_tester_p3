#!/usr/bin/python3.5
#coding:utf-8
import xmltodict as xd
import json

class XmlTransfer():
    def __init__(self):
        pass

    #定义xml转换字典方法
    def xml_to_dict(self,xmlstr):
        try:
            trans_str=xd.parse(xmlstr)
            json_data=json.dumps(trans_str)
            json_data=json.loads(json_data)
            return json_data
        except Exception as e:
            print(e)

    #定义字典转换xml方法
    def dict_to_xml(self,dict_data={}):
        try:
            if len(dict_data.items())==1:
                return xd.unparse(dict_data)
            else:
                raise ValueError('wrong frame of dict')
        except Exception as e:
            print(e)


if __name__=="__main__":
    test_str="<student><info><mail>xxx@xxx.com</mail><name>name</name><sex>male</sex></info><course><score>90</score><name>math</name></course><course><score>88</score><name>english</name></course><stid>10213</stid></student>"
    a= XmlTransfer().xml_to_dict(test_str)
    print(a)
    b=XmlTransfer().dict_to_xml(a)
    print(b)