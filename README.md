Laurasaur
=========

Laurasaur is a collection of python scripts designed to make Laura's life easier. Each script has a single purpose. To run these scripts, you must first set up Python 2.7+ on your computer. For this, I recommend downloading the appropriate distribution from http://www.activestate.com/activepython/downloads and following the installation instructions.



##1) Spreadsheet Campaign
Given an Excel .xls spreadsheet with the required columns, gmail account credentials, and a text file with Python-formatted parameter placeholders, will send an email to each sendto email address row (one email per row).

In this document, the "headers" or "column header" refers to the value of the cell in the top row of a spreadsheet.

Python-formatted parameter placeholders in the template means that if you put "{firstName}" in the text (no quotes), the curly brackets {} and the name inside would be replaced with the value of the spreadsheet cell of the column with header "firstName" (no quotes) and the current row being used to send an email when the script is run.

To use Spreadsheet Campaign, run the IDLE application that came with ActiveState python (should be in your C:\Python27 directory) and open LaurasaurSpreadsheetTest.py. Edit the values in this file to match the spreadsheet and message template with which you want to send emails. 

DEPENDENCIES:
=> You will need to install xlrd, which can be acquired from: http://pypi.python.org/pypi/xlrd

### The Values You Edit Are: ###

  template = 'D:\Dev\Laurasaur\Laurasaur\SpreadsheetCampaign\DemoCampaignTemplate.txt'

  data = 'D:\Dev\Laurasaur\Laurasaur\SpreadsheetCampaign\DemoCampaignSpreadsheet.xls'

  sendFromGmailAddress = 'youremail@gmail.com'

  sendFromGmailUserName = 'yourGmailUserName'

  sendFromGmailPassword = 'yourGmailPassword'

### Setting Up The Data Spreadsheet ###
There are 5 required columns in the Data Spreadsheet that are required. All other columns, if they are included, will be available as parameters that you can reference in the template by their column header. All column headers must be unique within a spreadsheet.

  ToPrefix   => the prefix of the person to whom this message is addressed

  ToName     => the name of the person to whom this message is addressed

  ToAddress  => the email address to send this message to

  FromName   => the name to show in the receiver's inbox as From

  Subject    => the mail subject

### Running The Campaign (script)
When you are done editing the values, save the file, and choose Run => Run Module from the menu at the top.
