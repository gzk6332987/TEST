from socket import *


def main():
    # TCP套接字
    TCP_server = socket(AF_INET, SOCK_STREAM)
    TCP_server.bind(("127.0.0.1", 8765))

    # 改为监听套接字
    print("正在监听")
    TCP_server.listen(10)

    # 为客户端服务
    print("正在改为为客户端服务")
    new_socket, socket_addr = TCP_server.accept()

    # 读取内容
    print("等待读取内容")
    new_socket.recv(1024)

    # 发送信息(不解析)
    response = "HTTP/1.1 200 OK\n"
    response += "\n"
    response += "Hallo world."

    new_socket.send(response.encode("utf-8"))


if __name__ == "__main__":
    main()
