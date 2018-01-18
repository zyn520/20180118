import requests
from bs4 import BeautifulSoup

url='http://www.cnblogs.com/yoyoketang/'
r1=requests.get(url)
content=r1.content

#用html.parser解析页面
soup=BeautifulSoup(content,'html.parser')

#获取所有class属性为dayTitle
time=soup.find_all(class_="dayTitle")
for i in time:
   # a=i
    print(i.a.string)