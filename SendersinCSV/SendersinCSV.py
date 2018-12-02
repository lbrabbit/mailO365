import sys
sys.path.append('..')
import pandas as pd
import faddr
import getpass
import myemailib

df = pd.read_csv("GroupLeader.csv",index_col=0)
fromaddr = faddr.faddr
passwd = getpass.getpass('Password: ')  
for index, row in df.iterrows():
  print (index+"@student.hkcc-polyu.edu.hk", "%02d" % row['Grp'], row['Name'])

  toaddr = index+"@student.hkcc-polyu.edu.hk"
  body = "Dear Group Leader "+row['Name']+","
  body += """

Please find the attached mark sheet for your group project and inform your group members.

Regards,

Haggen"""
  directory = "./pdf"
  filename = "CCN1031_Group_Project_Marking_%02d.xls.pdf" % row['Grp']

  server = myemailib.email_login(fromaddr, passwd)
  msg = myemailib.create_msg(fromaddr, toaddr, "CCN1031 Group Project Mark", body)
  myemailib.attach_msg(directory, filename, msg)

  text = msg.as_string()
  server.sendmail(fromaddr, toaddr, text)
  input("Press Enter to continue...")

server.quit()
