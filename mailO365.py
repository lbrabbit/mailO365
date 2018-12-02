# https://stackoverflow.com/questions/46160886/how-to-send-smtp-email-for-office365-with-python-using-tls-ssl
# https://stackoverflow.com/questions/9202224/getting-command-line-password-input-in-python
# http://naelshiab.com/tutorial-send-email-python/
# https://docs.python.org/3.4/library/email-examples.html

import os
import smtplib
import getpass
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
 
fromaddr = 'hhhhsoso@hkcc-polyu.edu.hk'
toaddr = "haggenso@gmail.com"
passwd = getpass.getpass('Password: ')

server = smtplib.SMTP('smtp.office365.com', 587)
server.ehlo()
server.starttls()
server.login(fromaddr, passwd)

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "SUBJECT OF THE MAIL"
body = "YOUR MESSAGE HERE"
msg.attach(MIMEText(body, 'plain'))

directory = "."
filename = "test.txt"
path = os.path.join(directory, filename)
with open(path, 'rb') as fp:
  attach = MIMEBase("application","octet-stream")
  attach.set_payload(fp.read())
# Encode the payload using Base64
encoders.encode_base64(attach)
attach.add_header('Content-Disposition', 'attachment', filename=filename)
msg.attach(attach)

text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)

server.quit()
