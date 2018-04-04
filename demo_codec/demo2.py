import codecs
for i in range(65, 122):
    c = chr(i)              # 数字转字符
    c = bytes(c, 'utf-8')   # 字符转字节
    ret = codecs.encode(bytes(c), 'hex_codec')  # 字节转换成十六进制
    #print('{}->{}'.format(c,ret))
    print('{}'.format(str(ret, 'utf-8')))       # 十六进制转换为字符串