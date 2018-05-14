import struct

demo = [1, 2.2, b'a', b'aaaa']          # 如果想要传递字符串，必须是字节型
packDemo = struct.pack('Ifs4s', *demo)  # *demo返回的是demo列表里的各个值
print('Pack demo:', packDemo)           # Pack demo: b'\x01\x00\x00\x00\xcd\xcc\x0c@aaaaa'
unPackDemo = struct.unpack('Ifs4s', packDemo)
print('Unpack demo:', unPackDemo)       # Unpack demo: (1, 2.200000047683716, b'a', b'aaaa')



