import socket
sk = socket.socket()
address = ('127.0.0.1', 8888)
sk.connect(address)
send_data = input('输入发送内容：')
sk.sendall(bytes(send_data.encode('utf-8')))
accept_data = sk.recv(1024).decode('utf-8')
print(type(accept_data))
print('接收内容：{}'.format(accept_data))