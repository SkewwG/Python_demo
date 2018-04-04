import binascii

print(help(binascii.hexlify))
print(binascii.hexlify('qwertyuiopasdfgh'.encode('utf-8')))


import chardet
a = '中'.encode('utf-8')
print('中'.encode('utf-8'))          # b'\xe4\xb8\xad'
print(chardet.detect(a))
print(len('中'))