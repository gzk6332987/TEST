import re
from socket import *
import datetime
import threading
import web_mini

# 全局变量
str_html = 'html'


class My_server(object):
    def __init__(self, ip, port):
        # 定义
        self.op = None
        self.addr = None
        self.new_socket = None
        self.headers = ''
        self.status = ''

        # 套接字初始化
        self.tcp_server = socket(AF_INET, SOCK_STREAM)
        self.tcp_server.bind((ip, port))
        self.tcp_server.listen(10)

    def run(self):
        """
        周而复始的运行
        :return:
        """
        while True:
            self.new_socket, self.addr = self.tcp_server.accept()
            self.accept()

    def accept(self):
        """
        接收数据并使用re模块,接力到judge(),若接收到空值,直接执行end()
        :return:
        """
        get = self.new_socket.recv(1024).decode("utf-8")
        if not get:
            self.end()
        the_first_line = get.splitlines()[0]
        self.get = re.match('\w+ (/.*)[ ]', the_first_line).group(1)
        print("正则GET到的信息为:%s" % self.get)
        # 接力
        self.judge()

    def judge(self):
        """
        进行判断,返回静态,动态页面
        :return:
        """
        if self.get.endswith(".py"):
            # 进行动态函数
            self.dynamic()
        if self.get == '/':
            file_path = str_html + '/index.html'
            # 返回静态主页
            self.op = open(file_path, "rb")
            self.send()
        else:
            # 判断是否存在指定页面
            file_path = str_html + self.get
            try:
                self.op = open(file_path, "rb")
                self.send()
            except:
                self.error()


    def dynamic(self):
        """
        返回动态页面
        :return:
        """
        response_body = web_mini.application(self.get, self.set_h_b, self.error)
        response_head = 'HTTP/1.1 200 OK\n\r'
        response_head += 'Content-Type:text/html\n\r\n\r'
        # 返回页面
        self.new_socket.send(response_head.encode('utf-8'))
        self.new_socket.send(response_body)

    def set_h_b(self, status, headers):
        self.status = status
        self.headers = headers

    def send(self):
        """
        发送静态页面
        :return:
        """
        rd = self.op.read()
        response_head = "HTTP/1.1 200 OK\n\r"
        response_head += "Content-Type:text/html\n\r\n\r"
        response_body = rd
        # 发送
        self.new_socket.send(response_head.encode('utf-8'))
        self.new_socket.send(response_body)
        # 执行end()
        self.end()

    def error(self):
        """
        返回404页面
        :return:
        """
        response_head = "HTTP/1.1 404 file not found\n\r"
        response_head += "Content-Type:text/html;charset=utf-8\r\n\n\r"
        try:
            response_body = open("html/error.html", "rb").read()#.replace(bytes("file not", encoding='utf-8'), bytes("you", encoding='utf-8'))
        except:
            response_body = "error.html not found.Maybe we del it or moved it!".encode("utf-8")
        # 发送头和身体
        self.new_socket.send(response_head.encode("utf-8"))
        self.new_socket.send(response_body)
        # 执行end()
        self.end()

    def end(self):
        """
        循环最后,关闭套接字
        :return:
        """
        self.new_socket.close()
        return


def main():
    # 初始化
    ip = 'localhost'
    port = 8888

    s = My_server(ip, port)
    s.run()


if __name__ == '__main__':
    main()
