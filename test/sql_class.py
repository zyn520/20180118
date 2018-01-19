import pymysql

class mySql():
    def __init__(self):
        #创建连接
        self.con=pymysql.connect(host='192.168.0.241',port=3306,user='root',password='root',db='zfy-source')
        self.curser=self.con.cursor()
    def exe_sql(self,sql):
        self.curser.execute(sql)
        self.con.commit()
    def close_con(self):
        self.curser.close()
        self.con.close()

if __name__ == '__main__':
    a=mySql()
    sql='insert into zfy_device values(2,"asff","000123456789","1","mysql","","1","5/24/2017","0","3","5","0","2018-01-18 17:25:31","1029","admin","0","105","105")'
    a.exe_sql(sql)
    a.close_con()

