import socket, ssl, time

# python 3.3 begin
# context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
# context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")
# python 3.3 end

bindsocket = socket.socket()
print("socket create success")
bindsocket.bind(('192.168.103.2', 10023))
print("socket bind success")
bindsocket.listen(5)
print("socket listen success")


def do_something(connstream, data):
    print("data length:", len(data))
    return True


def deal_with_client(connstream):
    t_recv = 0
    t_send = 0
    n = 0
    t1 = time.clock()
    data = connstream.recv(1024)
    t2 = time.clock()
    print("receive time:", t2 - t1)
    # empty data means the client is finished with us
    while data:
        if not do_something(connstream, data):
            # we'll assume do_something returns False
            # when we're finished with client
            break
        n = n + 1
        t1 = time.clock()
        send_data = input('输入发送内容：')
        connstream.send(bytes(send_data.encode('utf-8')))
        t2 = time.clock()
        t_send += t2 - t1
        print("send time:", t2 - t1)
        t1 = time.clock()
        accept_data = connstream.recv(1024).decode('utf-8')
        t2 = time.clock()
        t_recv += t2 - t1
        print("receive time:", t2 - t1)
        print('接受内容：{}'.format(accept_data))
    print("avg send time:", t_send / n, "avg receive time:", t_recv / n)
    # finished with client


while True:
    newsocket, fromaddr = bindsocket.accept()
    print("socket accept one client")
    # python 3.3 begin
    # connstream = context.wrap_socket(newsocket, server_side=True)
    # python 3.3 end

    # python 2.x begin
    connstream = ssl.wrap_socket(newsocket, "key.pem", "cert.pem", server_side=True, ssl_version=ssl.PROTOCOL_TLSv1)
    # python 2.x end
    try:
        deal_with_client(connstream)
    finally:
        connstream.shutdown(socket.SHUT_RDWR)
        connstream.close()