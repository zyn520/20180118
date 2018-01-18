from selenium import webdriver
from requests import cookies
import unittest
import requests
from time import sleep

s=requests.session()
r1=s.get("http://192.168.0.241:8080/login")
c={'COOKIE_SSID_ATTR':'0376cd10134f4304b0f5c0c1eff22366',
   'COOKIE_USER_ATTR': '429',
   'COOKIE_COMPANY_ID_ATTR':'29'}
requests.utils.add_dict_to_cookiejar(s.cookies, c)


url2="http://192.168.0.241:8080/device/search"
datas={"pageNumber":"1",
      "pageSize":"10",
      "keywords":""}
head2={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
       "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8"}
r2=s.post(url=url2,data=datas,headers=head2)
#print(r2.status_code)
