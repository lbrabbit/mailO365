import sys
import pandas as pd
import getpass
import time

# Import my libraries
sys.path.append('..')
import myemailib
import faddr

df = pd.read_csv("A2.csv",index_col=0)
# My email is hidden in faddr.py, replace with your email below
fromaddr = faddr.faddr
passwd = getpass.getpass('Password: ')  
for index, row in df.iterrows():
  print (index+"@student.hkcc-polyu.edu.hk")

  # For Testing
  # toaddr = fromaddr
  toaddr = index+"@student.hkcc-polyu.edu.hk"
  body = "Dear Student"+","
  body += """

Please find the attached mark sheet for your Access In-Class Exercise. Also, the group project mark sheet was delivered to your group leader.

Regards,

Haggen"""
  directory = "./pdf"
  filename = index+" (Marking) Access CCN1031.pdf"

  server = myemailib.email_login(fromaddr, passwd)
  msg = myemailib.create_msg(fromaddr, toaddr, "CCN1031 Access In-Class Mark", body)
  myemailib.attach_msg(directory, filename, msg)

  text = msg.as_string()
  server.sendmail(fromaddr, toaddr, text)
  #input("Press Enter to continue...")
  time.sleep(2)

server.quit()
