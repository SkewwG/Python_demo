import smtplib

smtp = smtplib.SMTP()
smtp.connect("mx3.qq.com", "25")
smtp.login('用户名', '密码')
smtp.sendmail('from@yeah.net', 'to@21cn.com',
              'From: from@yeah.net/r/nTo: to@21cn.com/r/nSubject: this is a email from python demo/r/n/r/nJust for test~_~')
smtp.quit()