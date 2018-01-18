import requests
from bs4 import BeautifulSoup

url1='https://www.jianshu.com/u/03cf7ea68bf7'
r1=requests.get(url1,verify=False)
content=r1.content
print(content)
print(r1.status_code)
soup=BeautifulSoup(content,'html.parser')

author=soup.find_all(class_='content')

for i in author:
    print(i.p.string)



