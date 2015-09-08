#!/bin/sh

if [ $# -eq 1 ]; then
	echo "[+] Run socat..."
	echo "[+] Program: $1"
	echo "[+] Default Port: 12345"
	socat TCP-LISTEN:12345,reuseaddr,fork,bind=localhost EXEC:"$1"

elif [ $# -eq 2 ]; then
	echo "[+] Run socat..."
	echo "[+] Program: $1"
	echo "[+] Port: $2"
	socat TCP-LISTEN:$2,reuseaddr,fork,bind=localhost EXEC:"$1"

else
        echo "USAGE:: superd [Program Path] [Port]"

fi


