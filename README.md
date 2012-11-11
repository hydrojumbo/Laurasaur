Laurasaur
=========

Like a regular Laura, with purple horns.

Laurasaur is a collection of python scripts designed to make Laura's life easier. Each script has a single purpose. To run these scripts, you must first set up Python 2.7+ on your computer. For this, I recommend downloading the appropriate distribution from http://www.activestate.com/activepython/downloads and following the installation instructions.

Scripts available:

1) Spreadsheet Campaign => given an Excel .xls or .xlsx spreadsheet with the required columns, gmail account credentials, and a text file with Python-formatted parameter placeholders ({firstName} replaces the curly brackets {} and the name inside with the value of the column with header "firstName" for the row being used to send an email now), will send an email to each sendto email address row (one email per row).