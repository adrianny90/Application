@echo off

for f tokens=2 delims== %%a in ('wmic OS Get localdatetime value') do set dt=%%a
set YY=%dt~2,2% & set YYYY=%dt~0,4% & set MM=%dt~4,2% & set DD=%dt~6,2%
set HH=%dt~8,2% & set Min=%dt~10,2% & set Sec=%dt~12,2%
set datestamp=%YYYY%%MM%%DD% & set timestamp=%HH%%Min%%Sec%
set fullstamp=%YYYY%-%MM%-%DD%_%HH%-%Min%-%Sec%

net use 10.163.30.113plc 1 userAdministrator
copy 10.163.30.113plcRackData.json %~dp0GFTXCrane1
cd %~dp0GFTXCrane1
rename  RackData.json RackData_%datestamp%_%timestamp%.json
echo BACKUP CRANE-1 COMPLETE!

net use 10.163.30.123plc 1 userAdministrator
copy 10.163.30.123plcRackData.json %~dp0GFTXCrane2
cd %~dp0GFTXCrane2
rename  RackData.json RackData_%datestamp%_%timestamp%.json
echo BACKUP CRANE-2 COMPLETE!

net use 10.163.30.133plc 1 userAdministrator
copy 10.163.30.133plcRackData.json %~dp0GFTXCrane3
cd %~dp0GFTXCrane3
rename  RackData.json RackData_%datestamp%_%timestamp%.json
echo BACKUP CRANE-3 COMPLETE!

net use 10.163.30.143plc 1 userAdministrator
copy 10.163.30.143plcRackData.json %~dp0GFTXCrane4
cd %~dp0GFTXCrane4
rename  RackData.json RackData_%datestamp%_%timestamp%.json
echo BACKUP CRANE-4 COMPLETE!

net use 10.163.30.153plc 1 userAdministrator
copy 10.163.30.153plcRackData.json %~dp0GFTXCrane5
cd %~dp0GFTXCrane5
rename  RackData.json RackData_%datestamp%_%timestamp%.json
echo BACKUP CRANE-5 COMPLETE!

net use 10.163.30.163plc 1 userAdministrator
copy 10.163.30.163plcRackData.json %~dp0GFTXCrane6
cd %~dp0GFTXCrane6
rename  RackData.json RackData_%datestamp%_%timestamp%.json
echo BACKUP CRANE-6 COMPLETE!




net use 10.163.30.193plc 1 userAdministrator
copy 10.163.30.193plcRackData.json %~dp0GFTXCrane9
cd %~dp0GFTXCrane9
rename  RackData.json RackData_%datestamp%_%timestamp%.json
echo BACKUP CRANE-9 COMPLETE!

net use 10.163.30.203plc 1 userAdministrator
copy 10.163.30.203plcRackData.json %~dp0GFTXCrane10
cd %~dp0GFTXCrane10
rename  RackData.json RackData_%datestamp%_%timestamp%.json
echo BACKUP CRANE-10 COMPLETE!

net use 10.163.30.213plc 1 userAdministrator
copy 10.163.30.213plcRackData.json %~dp0GFTXCrane11
cd %~dp0GFTXCrane11
rename  RackData.json RackData_%datestamp%_%timestamp%.json
echo BACKUP CRANE-11 COMPLETE!

net use 10.163.30.223plc 1 userAdministrator
copy 10.163.30.223plcRackData.json %~dp0GFTXCrane12
cd %~dp0GFTXCrane12
rename  RackData.json RackData_%datestamp%_%timestamp%.json
echo BACKUP CRANE-12 COMPLETE!


@pause





