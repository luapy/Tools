#2018.12.6

import subprocess
import pexpect
import sys


def AccountList(number):
	ten=["root","1.1.1.1","22"]#用户 ip 端口
	BAN=["root","2.2.2.2","22"]
	JANPan=["root","3.3.3.3","22"]
	Account=[]
	if number == '1':
		Account=ten
	elif number =='2':
		Account=BAN
	elif number =='3':
		Account=JANPan
	return Account
def connect(name_ip,port):
	port="-p "+str(port)
#child = winpexpect.winspawn("ssh root@ -p ")
	child = subprocess.run(["ssh",name_ip,port,])
	#try:
		#if (child.expect([pexpect.TIMEOUT,'password'])):
			#child.sendline('')
	#except:
		#print(str(child))

def main():
	print("1. 1.1.1.1(腾讯云)")
	print("2. 1.1.1.1(搬瓦工)")
	print("3. 1.1.1.1(Janpan)")
	ssh_num = input("please choose one:\n")
	Account=[]
	Account=AccountList(ssh_num)
	name_ip=Account[0]+"@"+Account[1]
	port=Account[2]
	connect(name_ip,port)

main()
