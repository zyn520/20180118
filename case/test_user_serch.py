from requests import cookies
import unittest
from case import login214
from common import logger
import requests

class user_Search(unittest.TestCase):
    log=logger.Log()
    def setUp(self):
        s=requests.session()
        self.s=s
        self.login=login214.Login(s).login()

    def test_usersearch(self):
        self.log.info('开始测试人员管理查询')
        url='http://192.168.0.241:8080/system/user/search'
        data={"pageNumber": "1",
                 "pageSize": "10",
                 "keywords": ""}
        r=self.s.post(url,data=data,verify=False)
        self.assertEqual(200,r.status_code)
        self.log.info('响应为'+str(r.status_code))
        result=r.json()
        self.assertEqual(929,result['total'])
        self.log.info('人员总数为'+str(result['total']))
if __name__ == '__main__':
    unittest.main()
