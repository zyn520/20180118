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


