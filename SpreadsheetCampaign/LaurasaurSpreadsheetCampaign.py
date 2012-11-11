import smtplib  
import email.utils
from email.mime.text import MIMEText
import xlrd
import sys

#template, spreadsheet, fromAddress, username, password
def main(arg1, arg2, arg3, arg4, arg5):
    #f = open('D:\Dev\Laurasaur\Laurasaur\SpreadsheetCampaign\DemoCampaignTemplate.txt', 'r')
    f = open(arg1, 'r')
    template = f.read()

    #wb = xlrd.open_workbook('D:\Dev\Laurasaur\Laurasaur\SpreadsheetCampaign\DemoCampaignSpreadsheet.xls')
    wb = xlrd.open_workbook(arg2)
    s = wb.sheets()[0]

    # Credentials 
    fromAddr = arg3
    username = arg4
    password = arg5
    server = smtplib.SMTP('smtp.gmail.com:587')  
    server.starttls()  
    server.login(username,password)
            
    first = 0
    keys = []
    print template
    for row in range(s.nrows):
        values = {}
        if (first == 0):
            first = 1
            for col in range(s.ncols):
                keys.append(s.cell(row,col).value)        
        else:
            for col in range(s.ncols):
                values[keys[col]] = s.cell(row,col).value
            #print values
            #print template.format(**values)
            
            msg = MIMEText(template.format(**values))
            msg['To'] = email.utils.formataddr((values['ToPrefix'] + ' ' + values['ToName'], values['ToAddress']))
            msg['From'] = email.utils.formataddr((values['FromName'], fromAddr))
            msg['Subject'] = values['Subject']

            print msg        
              
            # The actual mail send          
            server.sendmail(fromAddr, values['ToAddress'], msg.as_string())            
        print

    server.quit()  
    return 0

if __name__=='__main__':
    sys.exit(main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]))
    

#msg = MIMEText('Apparently, all of that jazz is just a matter of adding "Headers" to the email message body.')
#msg['To'] = email.utils.formataddr((toname, toaddr))
#msg['From'] = email.utils.formataddr((fromname, fromaddr))
#msg['Subject'] = 'Ha... got it this time :)'
  
# Credentials (if needed)  
#username = 'yourgmailusername'  
#password = 'yourgmailpassword'  
  
# The actual mail send  
#server = smtplib.SMTP('smtp.gmail.com:587')  
##server.starttls()  
#server.login(username,password)
#server.sendmail(fromaddr, toaddr, msg.as_string())  
#server.quit()  
