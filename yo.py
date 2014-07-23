#!/usr/bin/python

import smtplib
import json
import os

sender = 'si.oh49@avg.co.kr'
receivers = ['ohbargain@icloud.com']
subject = "Yo."
message = "Yo."
with open(os.path.expanduser("~") + "/.yorc", "r") as f:
    login_json = json.loads(f.read())

message = """From: Yoer <{sender}>
To: Yoee <{receiver}>
Subject:{subject}
{message}
""".format(sender=sender,
           receiver=receivers[0],
           subject=subject,
           message=message)


try:
    smtpObj = smtplib.SMTP('mail.avg.co.kr')
    if login_json:
        smtpObj.login(login_json["smtp_login"], login_json["smtp_password"])
    smtpObj.sendmail(sender, receivers, message)
    print "Successfully sent email"
except smtplib.SMTPException:
    print "Error: unable to send email"
