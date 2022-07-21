import datetime
import re
import threading
from socket import *


class Server(object):

    def __init__(self, ip, port, log):
        self.log = log
        self.l = open(log, "a")
        self.l.write("***" * 5 + str(datetime.datetime.now()) + "***" * 5 + '\n')
        self.tcp = socket(AF_INET, SOCK_STREAM)
        while True:
            try:
                self.tcp.bind((ip, port))
                break
            except:
                port += 1
        self.tcp.listen(10)

    def run(self):
        while True:
            print("==========")
            self.new_socket, self.addr = self.tcp.accept()
            self.new_thread = threading.Thread(target=self.first_recv_datas())
            self.new_thread.start()
            # self.first_recv_datas()

    def first_recv_datas(self):
        self.msg = self.new_socket.recv(1024)
        if not self.new_socket:
            return

        self.r = re.match("\w+ (/.*)[ ]", self.msg.decode("utf-8"))
        if not self.r:
            return
        self.r = self.r.group(1)

        print("get到的信息:", self.r)
        self.second_return_pages()

    def second_return_pages(self):
        if self.r == '/':
            file = './index.html'
            self.f = open(file, "rb")
            self.read = self.f.read()

        else:
            try:
                # noinspection PyTypeChecker
                self.f = open('.' + self.r, "rb")
                self.read = self.f.read()
            except:
                self.r = self.r + '.html'
                try:
                    self.f = open(self.r, "rb")
                    self.read = self.f.read()
                except:  # 404
                    self.response_head = 'HTTP/1.1 404 file not found\n\r\n\r'
                    self.response_body = 'File not found, please input the right page!'

                    self.new_socket.send(self.response_head.encode("utf-8") + self.response_body.encode("utf-8"))
                    with open(self.log, "a") as l:
                        l.write(
                            "!404" + str(datetime.datetime.now()) + str(self.addr) + "GET:" + str(self.r) + '\n')  # 日志
                        l.close()
                    return
        # 发送文件
        self.response_head = 'HTTP/1.1 200 OK\n\r\n\r'.encode("utf-8")
        self.response_body = self.read

        self.new_socket.send(self.response_head + self.response_body)

        try:
            self.f.close()
        except:
            pass
        self.new_socket.close()
        with open(self.log, "a") as l:
            l.write("200" + str(datetime.datetime.now()) + str(self.addr) + "GET:" + str(self.r) + '\n')
            l.close()


def main():
    log_file = 'looger.log'

    port = input("请输入端口:")
    ip = str("127.0.0.1")
    if port == '':
        port = 80

    try:
        port = int(port)
    except:
        print("请输入正确的端口!")
    else:
        s = Server(ip=ip, port=int(port), log=log_file)
        s.run()


if __name__ == "__main__":
    main()
