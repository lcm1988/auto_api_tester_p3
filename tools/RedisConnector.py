#!/usr/bin/python3.5
#coding:utf-8
import redis
from tools.Conf import Conf

class RedisConnector():
    def __init__(self,rds_conf):
        conf=Conf().get_conf('config.%s'%rds_conf)
        self.__rds=redis.Redis(connection_pool=redis.ConnectionPool(host=conf['HOST'],port=conf['PORT'],password=conf['AUTH'],))

    @property
    def rds(self):
        return self.__rds


if __name__=="__main__":
    a= RedisConnector('RDS_QA')
    print(a.rds.hgetall('video:info:12545'))
