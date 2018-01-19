import pymysql

class mySql():
    def __init__(self):
        #创建连接

        self.con=pymysql.connect(host='192.168.0.241',port=3306,user='root',password='root',db='zfy-source')
        self.curser = self.con.cursor()

    def exe_sql(self,sql):

        try:
            self.curser.execute(sql)
        except Exception as a:
            self.con.rollback() #执行失败就回滚
            print("执行失败：%s"%a)
        self.curser.close()
        self.con.commit()
    def close_con(self):
        #关闭数据库连接
        try:
            self.con.close()
        except Exception as a:
            print("数据库关闭异常： %s"%a)



