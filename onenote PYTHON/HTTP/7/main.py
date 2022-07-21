from socket import *
from datetime import *
import re
import threading

class server(object):
    def __init__(self, ip, port):
        self.tcp = socket(AF_INET,SOCK_STREAM)
        self.tcp.bind((ip,port))
        self.tcp.listen(10)
        self.run()

    def run(self):
        while True:
            print("=========="*2)
            self.new_socket, new_addr = self.tcp.accept()
            self.data()

    def data(self):
        self.msg = self.new_socket.recv(2048)
        if not self.msg:
            return
        else:
            self.msg_first_line = self.msg.splitlines()[0]
        self.re = re.match("\w+ (/.*)[ ]",self.msg_first_line.decode('utf-8'))
        self.re = str(self.re.group(1))
        print("GET到的信息:",self.re)

        self.page()
        pass

    def page(self):
        if self.re == '/':
            file = './html/index.html'
            self.read = open(file,'rb')
        else:
            try:
                file = './html' + str(self.re)
                self.read = open(file,'rb')

            except:
                self.new_socket.send("HTTP/1.1 404 file not found\n\r\n\r"
                                     "PLEASE INPUT THE RIGHT PAGE!".encode("utf-8"))
                return

        # 发送
        self.response_head = b'HTTP/1.1 200 OK\n\r\n\r'
        self.response_body = self.read

        self.new_socket.send(self.response_head)
        self.new_socket.send(f"{self.response_body}")


def main():
    ip = '127.0.0.1'
    port = 8888
    s = server(ip, port)
    s.run()

if __name__ == '__main__':
    main()