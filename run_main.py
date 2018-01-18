import unittest
import time
import HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import os
from config import readCfg
from common import logger
cur_path=os.path.dirname(__file__)
#第一步加载所有用例
def add_case(caseName='case',rule='test*.py'):
    case_path=os.path.join(cur_path,caseName)
    #如果不存在就创建一个
    if not os.path.exists(case_path):os.mkdir(case_path)
    print(case_path)
    #定义discover方法
    discover=unittest.defaultTestLoader.discover(case_path,
                                                 pattern=rule,
                                                 top_level_dir=None)
    return discover

#第二步运行所有用例
def run_case(all_case,reportName="report"):
    now=time.strftime('%Y-%m-%d-%H-%M-%S')
    report_path=os.path.join(cur_path,reportName)
    if not os.path.exists(report_path):os.mkdir(report_path)
    report_abspath=os.path.join(report_path,'report.html')
    print('report abspath :'+report_abspath)
    fp=open(report_abspath,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,
                                         title=u'设备搜索接口测试结果',
                                         description=u'用例执行情况')
    runner.run(all_case)
    fp.close()

#发送邮件
def send_mail(report_file,sender,reciver,smtpserver,port,psw):
    # 构造邮件根容器
    msg = MIMEMultipart()
    # 定义邮件主题
    subject = '接口测试-设备查询接口'
    # 邮件主题以及收发件人
    msg['from'] = sender
    msg['to'] = receiver
    msg['subject'] = subject
    # 邮件正文
    content = open(report_file, 'rb')
    main_body = content.read()
    body = MIMEText(main_body, 'html', 'utf-8')
    # 将正文添加到根容器
    msg.attach(body)
    # 添加附件
    att = MIMEText(main_body, 'base64', 'utf-8')
    att['Content-type'] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment;filename="report.html"'
    msg.attach(att)
    try:
        smtp = smtplib.SMTP_SSL(smtpserver, port)

    except:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver, port)

    # 用户名密码登录
    smtp.login(sender, psw)
    print('开始发送邮件')
    #发送邮件需要收发人及邮件
    smtp.sendmail(sender, receiver, msg.as_string())
    #退出
    smtp.quit()
    print('发送成功')

if __name__ == '__main__':

    all_case=add_case()
    run_case(all_case)
    cur_path=os.path.dirname(os.path.dirname(__file__))
    file=os.path.join(cur_path,r'report\report.html')  #获取报告
    #print(report_file)
    #邮箱配置
    sender=readCfg.sender
    receiver=readCfg.reciver
    psw=readCfg.psw
    port=readCfg.port
    smtpserver=readCfg.smtp_server
    #send_mail(file,sender,receiver,smtpserver,port,psw)

