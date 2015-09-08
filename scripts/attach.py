import os
import sys
 
if os.getuid() != 0:
        print "[-] You are not root"
        sys.exit(-1)
 
if len(sys.argv) < 2:
        print "USAGE:: attach [binary name] [script]"
        sys.exit(-1)
 
output = os.popen('ps aux | grep '+sys.argv[1]).read()
 
outputs = output.split('\n')
lastline = ""

i=len(outputs)-2
while i>= 0:
        try:
                pid = outputs[i].split(None)[1]
        except:
                i -= 1
                continue

        if int(pid) < os.getpid()-2:
                lastline = outputs[i]
                break
        i -= 1

try: 
	pid = lastline.split(None)[1]
except:
	print "[-] Fail to find pid, plz check remote binary is running"
	sys.exit(-1)

print "[*] Attach to "+ ' '.join(lastline.split(None)[-2:]) +" ("+pid+")"
 
if len(sys.argv) == 3:
        print "gdb -q --pid="+pid+" -x "+sys.argv[2]
        os.system("gdb -q --pid="+pid+" -x "+sys.argv[2])
else:
        print "gdb -q --pid="+pid
        os.system("gdb -q --pid="+pid)
