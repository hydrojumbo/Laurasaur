import smtplib  
import email.utils
from email.mime.text import MIMEText

fromname = 'Alex'
fromaddr = 'alex@alex.com
toname = 'Laura'
toaddr  = 'laura@laura.com'

msg = MIMEText('Apparently, all of that jazz is just a matter of adding "Headers" to the email message body.')
msg['To'] = email.utils.formataddr((toname, toaddr))
msg['From'] = email.utils.formataddr((fromname, fromaddr))
msg['Subject'] = 'Ha... got it this time :)'
  
# Credentials (if needed)  
username = 'yourgmailusername'  
password = 'yourgmailpassword'  
  
# The actual mail send  
server = smtplib.SMTP('smtp.gmail.com:587')  
server.starttls()  
server.login(username,password)
server.sendmail(fromaddr, toaddr, msg.as_string())  
server.quit()  
