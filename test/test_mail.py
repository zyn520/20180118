import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.header import Header
from email import encoders
from config import readCfg
import os
#
def send_mail(report_file,sender,reciver,smtpserver,port,psw):
    subject='17号发送'
    #构造根容器
    email_obj=MIMEMultipart()
    #构造邮件主题
    email_obj['subject']=subject
    #构造邮件收发人
    email_obj['from']=sender
    email_obj['to']=reciver

    #构造邮件正文

    content=open(report_file,'rb')
    main_body=content.read()
    body=MIMEText(main_body,'html','utf-8')
    #将正文添加到根容器
    email_obj.attach(body)

    #添加附件
    att=MIMEText(main_body,'base64','utf-8')
    att['Content-type'] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment;filename="report.html"'
    #将附件添加到根容器
    email_obj.attach(att)

    #连接服务器
    smtp=smtplib.SMTP_SSL(smtpserver,port)

    #登录
    smtp.login(sender,psw)
    print('开始发送邮件')
    #发送邮件，需要sender，收件人，以及邮件
    smtp.sendmail(sender, reciver, email_obj.as_string())
    print('发送成功')
    #退出
    smtp.quit()

if __name__ == '__main__':
    cur_path=os.path.dirname(os.path.dirname(__file__))
    file=os.path.join(cur_path,r'report\report.html')
    sender=readCfg.sender
    reciver=readCfg.reciver
    smtpserver=readCfg.smtp_server
    port=readCfg.port
    psw=readCfg.psw
    send_mail(file,sender,reciver,smtpserver,port,psw)


