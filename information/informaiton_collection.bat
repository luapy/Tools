@echo off
echo ####information collection####
systeminfo > %USERPROFILE%\Desktop\collection.txt
ver >> %USERPROFILE%\Desktop\collection.txt
hostname>> %USERPROFILE%\Desktop\collection.txt
net user>> %USERPROFILE%\Desktop\collection.txt
net localgroup>> %USERPROFILE%\Desktop\collection.txt
net localgroup administrators>> %USERPROFILE%\Desktop\collection.txt
net user guest>> %USERPROFILE%\Desktop\collection.txt
net user administrator>> %USERPROFILE%\Desktop\collection.txt
echo ####at-with####>> %USERPROFILE%\Desktop\collection.txt
echo >> %USERPROFILE%\Desktop\collection.txt
echo ####task-list####>> %USERPROFILE%\Desktop\collection.txt
tasklist /svc>> %USERPROFILE%\Desktop\collection.txt
echo>> %USERPROFILE%\Desktop\collection.txt
echo ####net-work information####>> %USERPROFILE%\Desktop\collection.txt
ipconfig/all>> %USERPROFILE%\Desktop\collection.txt
route print>> %USERPROFILE%\Desktop\collection.txt
arp -a >> %USERPROFILE%\Desktop\collection.txt
netstat -an>> %USERPROFILE%\Desktop\collection.txt
ipconfig /displaydns>> %USERPROFILE%\Desktop\collection.txt
echo>> %USERPROFILE%\Desktop\collection.txt
echo ####service####>> %USERPROFILE%\Desktop\collection.txt
sc query type= service state = all>> %USERPROFILE%\Desktop\collection.txt
echo ####file####>> %USERPROFILE%\Desktop\collection.txt
cd \
tree /F>> %USERPROFILE%\Desktop\collection.txt
pause
