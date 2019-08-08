# DataUpdateAllPermits-
Files for updating data used by the application Tacoma Permits: https://wspdsmap.cityoftacoma.org/website/PDS/Permits/

Updates local json file (https) for application from CivicData table (http).

Place these files into the same folder with the following subfolders: 'data', 'log', and '_archive'.

1. Data_Download.py all permit records with a latitude/longitude value from CivicData as json.
2. Send_Email.vbs send email with results of running Data_Download.py.
4. UpdateData.bat makes a backup copy of yesterday's data, runs Data_Download.py, and creates a log file of results.

