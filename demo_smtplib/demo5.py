import smtplib
import dns.resolver

email = '446106525@qq.com'
username, domain = email.split('@')
mail_servers = dns.resolver.query(domain,'MX')

for mail_server in mail_servers:
    print('connect to {}'.format(str(mail_server.exchange)[:-1]))
    try:
        server = smtplib.SMTP(str(mail_server.exchange)[:-1])
        print('connect success!')
    except Exception as e:
        print('connect fail : {}'.format(e))