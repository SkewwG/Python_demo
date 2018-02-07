# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # 设置服务器
# mail_user = "ske_leton@163.com"  # 用户名
# mail_pass = "baige123456"  # 口令

# sender = 'ske_leton@163.com'
# receivers = ['skeletonbg@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
#
# message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
# message['From'] = Header("菜鸟教程", 'utf-8')
# message['To'] = Header("测试", 'utf-8')
#
# subject = 'Python SMTP 邮件测试'
# message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    print('access success!')
    # smtpObj.login(mail_user, mail_pass)
    # (code, msg) = smtpObj.helo('MailTester')
    # (code, msg) = smtpObj.docmd('MAIL FROM:', '<ske_leton@163.com>')
    # if 200 <= code <= 299:  # 发送邮件方的邮箱存在
    #     (code1, msg) = smtpObj.docmd('RCPT TO:', '<{}>'.format('skeletonasfsadfsadfbg@163.com'))
    #     print('code1 : {}'.format(code1))
    #     print('msg : {}'.format(msg))

except smtplib.SMTPException as e:
    print(e)
    print("Error: 无法发送邮件")