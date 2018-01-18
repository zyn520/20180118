import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from config import readCfg
#发送服务器
'''
smtpserver="smtp.qq.com"
port=465
sender='1521970772@qq.com'
psw='nhbfdtkmwpjlbadh'
receiver=['1521970772@qq.com','793260380@qq.com']
'''
def send_mail():
#邮件主题
    subject='这是我用脚本发送的'

#main_body='<p>这是发送的</p>'

#读文件
    cur_path=os.path.dirname(os.path.dirname(__file__))
    file=os.path.join(cur_path,r'report\report.html')
    fb=open(file,'rb')
    main_body=fb.read()
    msg=MIMEMultipart()
    msg['from']=readCfg.sender
    msg['to']=readCfg.reciver
    msg['subject']=subject
#邮件正文
    body=MIMEText(main_body,'html','utf-8')
    msg.attach(body)

#添加附件
    att=MIMEText(main_body,'base64','utf-8')
    att['Content-type']='application/octet-stream'
    att['Content-Disposition']='attachment;filename="report.html"'
    msg.attach(att)

#连接服务器
    smtp=smtplib.SMTP_SSL(readCfg.smtp_server,readCfg.port)
#像服务器标识用户身份
#smtp.helo(smtpserver)
#服务器返回确认结果
#smtp.ehlo(smtpserver)
#登录
    smtp.login(readCfg.sender,readCfg.psw)
#发送邮件
    print('开始发送')
    smtp.sendmail(readCfg.sender,readCfg.reciver,msg.as_string())
    print('发送成功')
#退出
    smtp.quit()
if __name__ == '__main__':
    send_mail()