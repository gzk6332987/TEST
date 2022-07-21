from socket import *
import re
import time
import datetime


class Server(object):
    def __init__(self, ip, port):
        self.tcp_server = socket(AF_INET, SOCK_STREAM)
        try:
            self.tcp_server.bind((ip, port))
        except:
            print(f"端口{port}可能被占用")
        # 改为监听
        self.tcp_server.listen(10)
        # 继续函数
        self.run_forever()

    def run_forever(self):
        while True:
            time.sleep(0.5)
            print("============"*2)
            log_path = "logger.log"
            self.lo = open(log_path,"a")

            self.new_socket, self.addr = self.tcp_server.accept()
            self.get_the_data()
            self.return_the_right_page()
            self.new_socket.close() #关闭套接字

            self.lo.close()

    def get_the_data(self):
        self.the_recv_data = self.new_socket.recv(1024).decode("utf-8")
        if self.the_recv_data:
            self.the_data = re.match("\w+ (/.*)[ ]", self.the_recv_data).group(1)
            print("get到的信息:", self.the_data)
            #记录日志
            self.lo.write("\n")
            self.lo.write("="*10)
            self.lo.write(str(datetime.datetime.now()))
            self.lo.write(self.the_data)
            self.lo.write(str(self.addr))

        else:
            #log
            with open("logger.log", "a") as l:
                l.write("\n" + str(datetime.datetime.now()) + "客户端返回空值")
            self.new_socket.close()
            self.run_forever()

    def return_the_right_page(self):
        if self.the_data == '/':
            the_path = "./index.html"
            f = open(the_path,"rb")
            response_head = "HTTP/1.1 200 OK\r\n\r\n"
            response_body = f.read()
            #发送东西给客户端
            self.new_socket.send(response_head.encode("utf-8"))
            self.new_socket.send(response_body)

        else:
            self.if_html = re.match("\w+ /.*html[ ]", self.the_recv_data)
            if self.if_html:
                try:
                    the_path = "." + self.the_data
                    f = open(the_path,"rb")
                    response_head = "HTTP/1.1 200 OK\r\n\r\n"
                    response_body = f.read()
                    # 发送东西给客户端
                    self.new_socket.send(response_head.encode("utf-8"))
                    self.new_socket.send(response_body)
                except:  # 404
                    self.return_404()
                    return
            else:
                the_path = "." + self.the_data + ".html"
                try:
                    f = open(the_path,"rb")
                    response_head = "HTTP/1.1 200 OK\r\n\r\n"
                    response_body = f.read()
                    self.new_socket.send(response_head.encode("utf-8"))
                    self.new_socket.send(response_body)
                except:
                    self.return_404()

    def return_404(self):
        response_head = "HTTP/1.1 404 file not found\r\n\r\n"
        response_body = "Please enter the right path!"
        self.new_socket.send(response_head.encode("utf-8"))
        self.new_socket.send(response_body.encode("utf-8"))

def main():
    # 设置ip和端口
    port = 8888
    ip = '127.0.0.1'

    log_file = "logger.log"
    with open(log_file,"a") as l:
        l.write("*"*10 + str(datetime.datetime.now()) + "*"*10)

    s = Server(port=port, ip=ip)

if __name__ == "__main__":
    main()
