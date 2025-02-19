# Download the file from `url` and save it locally under `file_name`
# Tacoma Permits from CivicData (json)
# Don't download any records without a lat/long.
# Updated: 2019-8-6
# Author: mmurnane

import urllib
import logging
import os

permitsResourceId = "11fac50d-5d1c-40e6-80b5-c339bd7b827c" #Changed 2019-8-6
theFields = "%22Permit_Number%22,%22Applied_Date%22,%22Latitude%22,%22Longitude%22,%22Address_Line_1%22,%22Permit_Type_Description%22,%22Current_Status%22,%22Issued_Date%22,%22Fees_Paid%22,%22Valuation%22,%22Description%22,%22Link%22"


#ALL PERMITS - 9.5 seconds browser load time
url = 'http://www.civicdata.com/api/3/action/datastore_search_sql?sql=SELECT%20' + theFields + '%20FROM%20%22' + permitsResourceId + '%22%20where%20%22Latitude%22%20%3C%3E%27%27%20and%20%22Longitude%22%20%3C%3E%20%27%27'

#Last 30 days - 7.5 seconds
#url = 'http://www.civicdata.com/api/3/action/datastore_search_sql?sql=SELECT%20' + theFields + '%20FROM%20%22' + permitsResourceId + '%22%20where%20%22Latitude%22%20%3C%3E%27%27%20and%20%22Longitude%22%20%3C%3E%20%27%27and%20%22Applied_Date%22%20%3E%20%272019-01-29%27'

#file_name = "\\\\wsitd01dev\\c$\\GADS\\website\\PDS\\Permits\\data\\Permits.json"  #DEV machine
file_name = "\\\\wsitd01\\c$\\GADS\\website\\PDS\\Permits\\data\\Permits.json"  #Production machine

try:
  # Download file 
  urllib.urlretrieve (url, file_name)
except:
  logging.exception('\n Unexpected error with website, could not download file successfully: \n')
else:
  if os.path.getsize(file_name)> 10000000:
    print "File download successful!"
  else:
    print "CHECK JSON FILE FOR ERROR MESSAGE! File download successful, but file size appears too small!"
