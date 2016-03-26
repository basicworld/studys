#!/usr/bin/python
#coding:utf-8
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import time
t=time.ctime()
sender = 'basicworld@163.com'
receiver = '382865134@qq.com'
subject = 'python email'
smtpserver = 'smtp.163.com'
username = 'basicworld@163.com'
password = 'WmjhB102749'

msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = 'vips.xls from python'

#构造附件
att = MIMEText(open('/var/ftpadmin/forwenjie/file_output/output.xls', 'rb').read(), 'base64', 'utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment; filename="vips.xls"'
msgRoot.attach(att)

smtp = smtplib.SMTP()
smtp.connect('smtp.163.com')
smtp.login(username, password)
smtp.sendmail(sender, receiver, msgRoot.as_string())
smtp.quit()
