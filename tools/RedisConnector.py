#!/usr/bin/python3.5
#coding:utf-8
import redis
from tools.Conf import Conf

class RedisConnector():
    def __init__(self,rdsconfig):
        #conf=Conf().get_conf('config.RDS_QA')
        self.__rds=redis.Redis(host=rdsconfig['HOST'],port=rdsconfig['PORT'],password=rdsconfig['AUTH'])

    @property
    def rds(self):
        return self.__rds


if __name__=="__main__":
    conf=Conf().get_conf('config.RDS_QA')
    a= RedisConnector(conf)
    a.rds.set('abc',123)
    a.rds.get('abc')
    #rds=redis.Redis(host='10.202.4.251',port=6342,password='0fd24ec8238c1c2f',)


