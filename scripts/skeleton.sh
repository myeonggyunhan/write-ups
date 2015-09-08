#!/bin/sh

if [ $# -eq 1 ]; then
	echo "[+] Make remote exploit skeleton ... "
	cp /home/leap/ShellScript/RemoteExploit_Skeleton.py exploit_tmp.py

	echo "[+] Set default host - localhost"
	echo "[+] Set port number  -" $1
	sed s/"port = 7777"/"port = $1"/ exploit_tmp.py > exploit.py

	rm exploit_tmp.py

elif [ $# -eq 2 ]; then
	echo "[+] Make remote exploit skeleton ... "
	cp /home/leap/ShellScript/RemoteExploit_Skeleton.py exploit_tmp.py

	echo "[+] Set host name   -" $1
	sed s/"host = 'localhost'"/"host = '$1'"/ exploit_tmp.py > exploit.py
	mv exploit.py exploit_tmp.py

	echo "[+] Set port number -" $2
	sed s/"port = 7777"/"port = $2"/ exploit_tmp.py > exploit.py
	
	rm exploit_tmp.py

else
	echo "USAGE:: skeleton [host name] [port number]"

fi




