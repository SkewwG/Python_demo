import codecs
for i in range(65, 122):
    c = chr(i)
    c = bytes(c, 'utf-8')
    ret = codecs.encode(bytes(c), 'hex_codec')
    print('{}->{}'.format(c,ret))