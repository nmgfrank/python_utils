# -*- coding: utf-8 -*-
import smtplib
from email.Header import Header
from email.mime.text import MIMEText


class Mail:
    def __init__(self):
        self.host = "mail.pset.suntec.net"
        self.port = "25"
        self.username = "redmine@pset.suntec.net"
        self.password = "111111Aa"
        self.mail_from = "redmine@pset.suntec.net"


    def send_mail(self,to_list,subject,content):
        if isinstance(content,unicode):
            content = str(content)
        me = ("%s<"+self.mail_from+">")%(Header('iRedmine','utf-8'),)
        to = ",".join(to_list)
        
        msg = MIMEText(content,'plain', 'utf-8')
        if not isinstance(subject,unicode):
            subject = unicode(subject)
        msg['Subject'] = subject
        msg['From'] = me
        msg['To'] = to
        msg['Accept-Language'] = 'zh-CN'
        msg['Accept-Charset'] = 'ISO-8859-1,utf-8'
    
        smtp = smtplib.SMTP()
        smtp.connect(self.host,self.port)
        smtp.login(self.username,self.password)
        smtp.sendmail(self.mail_from,to_list,msg.as_string())
        smtp.quit()
            



if __name__ == "__main__":
    mail = Mail()
    mail.send_mail(["liyunfei@pset.suntec.net"],"subject","content")
