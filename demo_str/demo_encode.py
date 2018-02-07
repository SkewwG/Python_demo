# 以 encoding 指定的编码格式编码字符串。errors参数可以指定不同的错误处理方案。
'''
encode(...)
    S.encode(encoding='utf-8', errors='strict') -> bytes

    Encode S using the codec registered for encoding. Default encoding
    is 'utf-8'. errors may be given to set a different error
    handling scheme. Default is 'strict' meaning that encoding errors raise
    a UnicodeEncodeError. Other possible values are 'ignore', 'replace' and
    'xmlcharrefreplace' as well as any other name registered with
    codecs.register_error that can handle UnicodeEncodeErrors.
'''
print(help(str.encode))
a = 'asdfsghjkl'
b = a.encode('utf-8')
print(b)                             # b = b'asdfsghjkl'