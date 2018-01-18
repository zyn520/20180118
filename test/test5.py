import unittest
import time
import HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import os
from config import readCfg
cur_path=os.path.dirname(__file__)



def send_mail(report_file,sender,receiver,smtpserver,port,psw):
    fb=open(report_file,'rb')
    main_body=fb.read()
    #定义邮件主题
    subject='接口测试-设备查询接口'
    #邮件内容
    msg=MIMEMultipart()
    msg['from']=sender
    msg['to']=receiver
    msg['subject']=subject
    #邮件正文
    body=MIMEText(main_body,'html','utf-8')
    msg.attach(body)
    #添加附件
    att = MIMEText(main_body, 'base64', 'utf-8')
    att['Content-type'] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment;filename="testresult12017-12-12-14_56_46.html"'
    msg.attach(att)
    try:
        smtp = smtplib.SMTP_SSL(smtpserver, port)
    except:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver, port)
    # 用户名密码
    smtp.login(sender, psw)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print('test report email has send out !')

if __name__ == '__main__':
    #report_path = os.path.join(cur_path, "report")  # 报告地址
    #print(report_path)
    #report_file=get_report(report_path)              #获取报告
    #print(report_file)
    #邮箱配置
    report_file= r'E:\2018\report\report.html'
    sender=readCfg.sender
    receiver=readCfg.reciver
    psw=readCfg.psw
    port=readCfg.port
    smtpserver=readCfg.smtp_server
    send_mail(sender, psw, receiver, smtpserver, report_file, port)
