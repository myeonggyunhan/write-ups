origin = 0x0a2e2e2e
counter = 0

while True:
	if (origin & 0xff000000) == 0x0:
		break
	origin = origin - 0x59
	counter+=1

print "[+] counter: " + str(counter)
print "[+] value: " + hex(origin)
	
