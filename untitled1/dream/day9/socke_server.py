import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):

        while True:
            self.data = self.request.recv(1024).strip()
            print(self.client_address[0])
            print(self.data)
            self.request.sendall(self.data.upper())     #给客户端返回

if __name__ == "__main__":
    HOST,PROT = "localhost",9000

    server = socketserver.ThreadingTCPServer((HOST,PROT),MyTCPHandler)

    server.serve_forever()