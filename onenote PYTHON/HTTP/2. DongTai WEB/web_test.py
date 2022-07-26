import socket
import re
import time

def handle_request(client_socket):
    """
    处理浏览器发送过来的数据
    然后回送相对应的数据（html、css、js、img。。。）
    :return:
    """
    # 1. 接收
    recv_content = client_socket.recv(1024).decode("utf-8", errors="ignore")

    print("-----接收到的数据如下----：")
    print(recv_content)
    lines = recv_content.splitlines()  # 将接收到的http的request请求数据按照行进行切割到一个列表中
    # for line in lines:
    #     print("---")
    #     print(line)

    # 2. 处理请求
    # 提取出浏览器发送过来的request中的路径
    # GET / HTTP/1.1
    # GET /index.html HTTP/1.1
    # .......
    lines[0]

    # 提取出/index.html 或者 /
    request_file_path = re.match(r"[^/]+(/[^ ]*)", lines[0]).group(1)

    print("----提出来的请求路径是：----")
    print(request_file_path)

    # 完善对方访问主页的情况，如果只有/那么就认为浏览器要访问的是主页
    if request_file_path == "/":
        request_file_path = "./index.html"

    try:
        # 从html文件夹中读取出对应的文件的数据内容
        with open(request_file_path, "rb") as f:
            content = f.read()
    except Exception:
        # 如果要是有异常，那么就认为：找不到那个对应的文件，此时就应该对浏览器404
        pass
        response_headers = "HTTP/1.1 404 Not Found\r\n"
        response_headers += "Content-Type:text/html;charset=utf-8\r\n"
        response_headers += "\r\n"
        response_boy = "----sorry，the file you need not found-------"
        response = response_headers + response_boy
        # 3.2 给浏览器回送对应的数据
        client_socket.send(response.encode("utf-8"))
    else:
        # 如果要是没有异常，那么就认为：找到了指定的文件，将其数据回送给浏览器即可
        response_headers = "HTTP/1.1 200 OK\r\n"
        response_headers += "Content-Type:text/html;charset=utf-8\r\n"
        response_headers += "\r\n"
        response_boy = content
        response = response_headers.encode("utf-8") + response_boy
        # 3.2 给浏览器回送对应的数据
        client_socket.send(response)

    # 4. 关闭套接字
    client_socket.close()


def main(ip,port):
    """
    用来控制整体
    :return:
    """

    # 1. 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 为了保证在tcp先断开的情况下，下一次依然能够使用指定的端口，需要设置
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 2. 绑定本地信息
    tcp_server_socket.bind((ip, port))

    # 3. 变成监听套接字
    tcp_server_socket.listen(128)

    while True:
        # 4. 等待客户端的链接
        client_socket, client_info = tcp_server_socket.accept()

        print(client_info)  # 打印 当前是哪个客户端进行了请求

        # 5. 为客户端服务
        handle_request(client_socket)

        # 6. 关闭套接字


if __name__ == '__main__':
    main(ip="127.0.0.1",port=8081)
