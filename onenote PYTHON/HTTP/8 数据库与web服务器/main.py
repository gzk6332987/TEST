import re
from socket import *
import threading
import datetime
import pymysql

class Server(object):
    def __init__(self, host, port):
        #套接字初始化
        self.tcp_server = socket(AF_INET,SOCK_STREAM)
        self.tcp_server.bind((host, port))
        self.tcp_server.listen(10)

        #pymysql初始化
        #......

        self.run()

    def run(self):
        while True:
            self.new_socket, self.addr = self.tcp_server.accept()
            print(datetime.datetime.now())
            if not self.new_socket:
                return
            else:
                print("有一个新连接:", self.addr)
            self.recv()

    def recv(self):
        self.msg = self.new_socket.recv(1024).decode("utf-8")
        if not self.msg:
            return
        self.msg_line = self.msg.splitlines()[0]
        print("GET到的信息:", self.msg_line)
        try:
            # GET / HTTP/1.1
            self.msg_re = re.match("\w+ (/.*)[ ]", self.msg_line)
            self.the_real_msg = self.msg_re.group(1)
            print("re后得到的信息:",self.the_real_msg)

            self.judge()

        except:
            print(f"地址为{self.addr}的返回有误!")
            error()

    def rp(self):   #如果正确,则返回
        try:
            self.read = self.f.read()
        except:
            self.error()
        self.response_head = 'HTTP/1.1 200 OK\n\r\n\r'.encode("utf-8")
        self.response_body = self.read

        self.new_socket.send(self.response_head)
        self.new_socket.send(self.response_body)
        return

    def error(self):    #如果错误,则返回
        self.response_head = 'HTTP/1.1 404 file not found\n\r\n\r'.encode("utf-8")
        self.response_body = 'File not found! Please enter the right addr!'.encode("utf-8")

        self.new_socket.send(self.response_head + self.response_body)
        return

    def judge(self):
        if self.the_real_msg == '/':
            self.file_name = './index.html'
            self.f = open(self.file_name,'rb')
            self.rp()

        else:
            self.file_name = '.' + self.the_real_msg
            try:
                self.f = open(self.file_name,'rb')
                self.rp()
            except:
                try:
                    self.file_name = self.file_name + ".html"
                    self.f = open(self.file_name,'rb')
                    self.rp()

                except:
                    self.error()


if __name__ == '__main__':
    s = Server(host='localhost', port=8888)
    s.run()