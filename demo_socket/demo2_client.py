import socket

sk = socket.socket()
sk.connect(('192.168.103.2', 8888))
while True:
    send_data = input('输入发送内容：')
    sk.sendall(bytes(send_data.encode('utf-8')))
    if send_data == 'exit':
        break
    accept_data = sk.recv(1024)
    print('接收内容：{}'.format(accept_data.decode('utf-8')))
sk.close()