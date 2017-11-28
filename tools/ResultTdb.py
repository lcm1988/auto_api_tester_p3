#coding:utf-8
import pymysql

'''
接收一个db连接配置，将结果存入到数据库
'''
class ResultTdb():
    def __init__(self,dbconfig):
        self.conf=dbconfig
        self.tbname=dbconfig['tb_name']

    '''
    values: 插入值，支持多行插入，例：[('lcm',20,85.35,'马驹桥'),('zht',21,80,'酒仙桥')]
    '''
    def saveres(self,values=[]):
        db= pymysql.connect(
            host=self.conf['host'],
            user=self.conf['user'],
            password=self.conf['pwd'],
            database=self.conf['db'],
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor
        )
        print('准备入库...')
        try:
            with db.cursor() as cursor:
                for i in values:
                    # 执行sql语句，插入记录
                    sql = '''insert into res (no,platform,casename,casepath,result,consoleinfo,errinfo,cost,uri,service) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
                    #sql = '''insert into res (no) values(%s)'''
                    cursor.execute(sql, (i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]))
                    # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
                    db.commit()
        finally:
            db.close()
        print('入库完毕')


if __name__=="__main__":
    from tools.Conf import Conf
    config=Conf().get_conf('config.REPORT_DB')
    data_fields={'data':'name,age','limit':'1'}
