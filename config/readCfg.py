import os
import configparser

cur_path=os.path.dirname(__file__)
cfgpath=os.path.join(cur_path,'cfg.ini')
cof=configparser.ConfigParser()
cof.read(cfgpath)

smtp_server=cof.get('email','smtpserver')
sender=cof.get('email','sender')
reciver=cof.get('email','receiver')
psw=cof.get('email','psw')
port=cof.get('email','port')