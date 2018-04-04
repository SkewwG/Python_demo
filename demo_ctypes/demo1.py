from ctypes import *

user32 = windll.LoadLibrary('user32.dll')           # 加载动态链接库
# user32.MessageBoxA(0, 'Ctypes is cool!', 'Ctypes', 0)       # 调用MessageBoxA函数
# print(user32)
PROCESS_ALL_ACCESS  =  ( 0x000F0000 | 0x00100000 | 0xFFF )
VIRTUAL_MEM  =  ( 0x1000 | 0x2000 )  # 12288
PAGE_EXECUTE_READWRITE  =  0x00000040
print(PROCESS_ALL_ACCESS)
print(VIRTUAL_MEM)
print(0x40)
print(0x0000000000270000-0x0000000000250000)