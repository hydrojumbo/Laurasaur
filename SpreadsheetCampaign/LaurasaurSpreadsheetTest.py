# dependencies of this .py module
import LaurasaurSpreadsheetCampaign

# parameters you set
template = 'D:\Dev\Laurasaur\Laurasaur\SpreadsheetCampaign\DemoCampaignTemplate.txt'
data = 'D:\Dev\Laurasaur\Laurasaur\SpreadsheetCampaign\DemoCampaignSpreadsheet.xls'
sendFromGmailAddress = 'youremail@gmail.com'
sendFromGmailUserName = 'yourGmailUserName'
sendFromGmailPassword = 'yourGmailPassword'

# do the email campaign
LaurasaurSpreadsheetCampaign.main(template, data, sendFromGmailAddress, sendFromGmailUserName, sendFromGmailPassword)
