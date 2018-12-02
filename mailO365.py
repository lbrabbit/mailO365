# https://stackoverflow.com/questions/46160886/how-to-send-smtp-email-for-office365-with-python-using-tls-ssl
# https://stackoverflow.com/questions/9202224/getting-command-line-password-input-in-python
# http://naelshiab.com/tutorial-send-email-python/
# https://docs.python.org/3.4/library/email-examples.html

import getpass
import myemailib
 
fromaddr = 'hhhhsoso@hkcc-polyu.edu.hk'
toaddr = "haggenso@gmail.com"
passwd = getpass.getpass('Password: ')
directory = "."
filename = "test.txt"

server = myemailib.email_login(fromaddr, passwd)
msg = myemailib.create_msg(fromaddr, toaddr, "SUBJECT OF THE MAIL", "YOUR MESSAGE HERE")
myemailib.attach_msg(directory, filename, msg)

text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)

server.quit()
