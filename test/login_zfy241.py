from selenium import webdriver
from requests import cookies
import unittest
import requests
from time import sleep

head1={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
      "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
      "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
       }
s=requests.session()
url="http://192.168.0.241:8080/login"
r1=s.get(url=url,headers=head1)
c=requests.cookies.RequestsCookieJar()
c.set('COOKIE_SSID_ATTR','0376cd10134f4304b0f5c0c1eff22366')
c.set('COOKIE_USER_ATTR','429')
c.set('COOKIE_COMPANY_ID_ATTR','29')


s.cookies.update(c)
sleep(2)
s.cookies['JSESSIONID']='BDD9B0FFDC579A07404DAB0CC98E03E3'
#s.cookies.set('JSESSIONID','456D2FECDD166305BD61A8AD53CF9BAC')
url="http://192.168.0.241:8080/login"

#r1=s.get(url=url,headers=c)
print(s.cookies)


url2="http://192.168.0.241:8080/device/search"
datas={"pageNumber":"1",
      "pageSize":"10",
      "keywords":""}
head2={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
       "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8"}
r2=s.post(url=url2,data=datas,headers=head2,allow_redirects=False)
#print(r2.status_code)
