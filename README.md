Laurasaur
=========

Like a regular Laura, with purple horns.

Laurasaur is a collection of python scripts designed to make Laura's life easier. Each script has a single purpose. To run these scripts, you must first set up Python 2.7+ on your computer. For this, I recommend downloading the appropriate distribution from http://www.activestate.com/activepython/downloads and following the installation instructions.

###Scripts available:###

1) Spreadsheet Campaign => given an Excel .xls spreadsheet with the required columns, gmail account credentials, and a text file with Python-formatted parameter placeholders ({firstName} replaces the curly brackets {} and the name inside with the value of the column with header "firstName" for the row being used to send an email now), will send an email to each sendto email address row (one email per row).

To use Spreadsheet Campaign, run the IDLE application that came with ActiveState python (should be in your C:\Python27 directory) and open LaurasaurSpreadsheetTest.py. Edit the values in this file to match the spreadsheet and message template you want to send emails with. 

### The Values You Edit Are: ###

  template = 'D:\Dev\Laurasaur\Laurasaur\SpreadsheetCampaign\DemoCampaignTemplate.txt'

  data = 'D:\Dev\Laurasaur\Laurasaur\SpreadsheetCampaign\DemoCampaignSpreadsheet.xls'

  sendFromGmailAddress = 'youremail@gmail.com'

  sendFromGmailUserName = 'yourGmailUserName'

  sendFromGmailPassword = 'yourGmailPassword'

### Required Columns In The Data Spreadsheet ###

  ToPrefix   => the prefix of the person to whom this message is addressed

  ToName     => the name of the person to whom this message is addressed

  ToAddress  => the email address to send this message to

  FromName   => the name to show in the receiver's inbox as From

  Subject    => the mail subject

When you are done editing the values, save the file, and choose Run => Run Module from the menu at the top.