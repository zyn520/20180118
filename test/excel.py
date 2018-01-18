import xlrd
import xlwt
from selenium import webdriver
from time import sleep
#获取Excel
data=xlrd.open_workbook(r'F:\test_login.xlsx')
print(data)

#获取Excel的某个sheet页的表
table=data.sheet_by_name('Sheet1')

#获取行数
row=table.nrows

#获取列数
col=table.ncols

#获取第一行的值
print(table.row_values(0))

#获取第一列的值
print(table.col_values(0))

print(table.row_values(1)[1])
driver=webdriver.Firefox()
driver.get('http://192.168.0.241:8080/login')
driver.find_element_by_id('loginName').send_keys(table.row_values(1)[0])
sleep(2)
driver.find_element_by_id('prepassword').send_keys(int(table.row_values(1)[1]))
