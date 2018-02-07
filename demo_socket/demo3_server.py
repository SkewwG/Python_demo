import socketserver
class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            conn = self.request
            addr = self.client_address
            while True:
                accept_date = conn.recv(1024).decode('utf-8')
                if accept_date == 'exit':
                    break
                print('接收内容：{}'.format(accept_date))
                send_data = input('输入发送内容：')
                conn.sendall(bytes(send_data.encode('utf-8')))
            conn.close()

if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 8888),MyServer)
    server.serve_forever()