import requests
from case import login214
import unittest
from common import logger

class element_Search(unittest.TestCase):
    log=logger.Log()
    def setUp(self):

        s = requests.session()
        self.s = s
        self.login=login214.Login(s).login()


    def test_search(self):
        self.log.info('开始测试')
        url2 = "http://192.168.0.241:8080/device/search"
        datas = {"pageNumber": "1",
                 "pageSize": "10",
                 "keywords": ""}
        head2 = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"}
        self.log.info('登录成功')

        r2 = self.s.post(url=url2, data=datas, headers=head2, allow_redirects=False)
        self.log.info('设备接口响应')
        self.assertEqual(200,r2.status_code)
        self.log.info('响应结果：' + str(r2.status_code))
        data=r2.json()
        self.assertEqual(0,data['total'])
        self.log.info('设备总数：'+str(data['total']))

if __name__ == '__main__':

    unittest.main()