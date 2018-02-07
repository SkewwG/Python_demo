import socket
sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sk.bind(('192.168.103.2',8888))
sk.listen(5)
while True:
    conn, addr = sk.accept()
    while True:
        accept_data = conn.recv(1024).decode('utf-8')
        print('接收内容：{}   客户端口：{}'.format(accept_data, addr[1]))
        if accept_data == 'exit':
            break
        send_data = input('输入发送内容：')
        conn.sendall(bytes(send_data.encode('utf-8')))
    conn.close()
