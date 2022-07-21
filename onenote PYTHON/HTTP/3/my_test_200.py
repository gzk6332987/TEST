import cgi
from socket import *
import time
import datetime
import re


def main(ip, port):
    # 创建套接字
    tcp_server = socket(AF_INET, SOCK_STREAM)

    # 绑定信息
    tcp_server.bind((ip, port))

    # 改为监听
    tcp_server.listen(124)

    # 给服务端服务
    while True:
        new_socket, addr = tcp_server.accept()
        print("=====连接地址=====\n", addr)
        serve(new_socket)
        new_socket.close()


def serve(new_socket):
    msg = new_socket.recv(1024).decode("utf-8",errors="ignore")      ##########################
    print("收到的信息为:\n", msg, "\n")
    msg_line = msg.splitlines()[0]
    print("\n\n",msg_line)

    # 使用re库调取信息
    # GET / HTTP/1.1
    # GET /index.html HTTP/1.1
    get = re.search(r"[ ][\w]*[ ](/[\w]*)[ ]", msg_line).group(1)
    print(print("get到的信息为:\n",get))


if __name__ == "__main__":
    main(ip="127.0.0.1", port=8081)
