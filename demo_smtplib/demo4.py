import smtplib

mailserver = "smtp.163.com:25"
try:
    svr = smtplib.SMTP(mailserver)
    print('connect ok')

except Exception as e:
    print(e)
