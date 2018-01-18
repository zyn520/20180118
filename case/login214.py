import requests
from requests import cookies

class Login():
    def __init__(self,s):
        self.s=s
        self.url="http://192.168.0.241:8080/login"
        self.head={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
      "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
      "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
       }
    def login(self):
        r1=self.s.get(self.url)
        c=requests.cookies.RequestsCookieJar()
        c.set('COOKIE_SSID_ATTR', 'd459ad9667f341a8a86b74d9a59bf0d5')
        c.set('COOKIE_USER_ATTR', '103')
        c.set('COOKIE_COMPANY_ID_ATTR', '5')
        self.s.cookies.update(c)
        self.s.cookies['JSESSIONID']='1231220D59D3F96F98ADA36F9FBCD38D'






