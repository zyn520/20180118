import pymysql

#创建连接
con=pymysql.connect(host='192.168.0.241',port=3306,user='root',password='root',db='zfy-source')

#建立游标
curser=con.cursor()

#执行sql
curser.execute('insert into zfy_device values(2,"asff","000123456789","1","mysql","","1","5/24/2017","0","3","5","0","2018-01-18 17:25:31","1029","admin","0","105","105")')
#有这句数据库插入数据显示
con.commit()

#关闭游标
curser.close()

#关闭连接
con.close()