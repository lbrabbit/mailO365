import os
import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText

def email_login(fromaddr, passwd):
  server = smtplib.SMTP('smtp.office365.com', 587)
  server.ehlo()
  server.starttls()
  server.login(fromaddr, passwd)
  return server

def create_msg(fromaddr, toaddr, subject, body):
  msg = MIMEMultipart()
  msg['From'] = fromaddr
  msg['To'] = toaddr
  msg['Subject'] = subject
  msg.attach(MIMEText(body, 'plain'))
  return msg

def attach_msg(directory, filename, msg):
  path = os.path.join(directory, filename)
  with open(path, 'rb') as fp:
    attach = MIMEBase("application","octet-stream")
    attach.set_payload(fp.read())
  # Encode the payload using Base64
  encoders.encode_base64(attach)
  attach.add_header('Content-Disposition', 'attachment', filename=filename)
  msg.attach(attach)
