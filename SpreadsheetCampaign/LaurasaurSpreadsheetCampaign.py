import smtplib  
import email.utils
from email.mime.text import MIMEText
import xlrd
import sys

#template, spreadsheet, fromAddress, username, password
def main(arg1, arg2, arg3, arg4, arg5):
    f = open(arg1, 'r')
    template = f.read()

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
            # get column headers 
            first = 1
            for col in range(s.ncols):
                keys.append(s.cell(row,col).value)        
        else:
            # send email message for the row.
            # required params in spreadsheet: 
            #     ToPrefix   => the prefix of the person to whom this message is addressed
            #     ToName     => the name of the person to whom this message is addressed
            #     ToAddress  => the email address to send this message to
            #     FromName   => the name to show in the receiver's inbox as From
            #     Subject    => the mail subject
            for col in range(s.ncols):
                values[keys[col]] = s.cell(row,col).value
            
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
    