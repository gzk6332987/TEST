import socket
import re
import multiprocessing
import mini_web


class Server(object):

    def __init__(self):
        # 1. 创建套接字
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 为了保证在tcp先断开的情况下，下一次依然能够使用指定的端口，需要设置
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # 2. 绑定本地信息
        self.tcp_server_socket.bind(("", 8081))

        # 3. 变成监听套接字
        self.tcp_server_socket.listen(128)

        # 定义2个属性，用来存储web框架传递过来的状态码以及响应头
        self.status = ""  # 指向状态码字符串
        self.headers = None  # 指向一个新的列表

    def handle_request(self, client_socket):
        """
        处理浏览器发送过来的数据
        然后回送相对应的数据（html、css、js、img。。。）
        :return:
        """
        # 1. 接收
        recv_content = client_socket.recv(1024).decode("utf-8", errors="ignore")

        print("-----接收到的数据如下----：")
        # print(recv_content)
        lines = recv_content.splitlines()  # 将接收到的http的request请求数据按照行进行切割到一个列表中
        # for line in lines:
        #     print("---")
        #     print(line)

        # 2. 处理请求
        # 提取出浏览器发送过来的request中的路径
        # GET / HTTP/1.1
        # GET /index.html HTTP/1.1
        # .......

        # 提取出/index.html 或者 /
        request_file_path = re.match(r"[^/]+(/[^ ]*)", lines[0]).group(1)

        print("----提出来的请求路径是：----")
        print(request_file_path)

        # 完善对方访问主页的情况，如果只有/那么就认为浏览器要访问的是主页
        if request_file_path == "/":
            request_file_path = "/index.html"

        # 如果请求的后缀不是.py结尾，那么就认为是普通的静态资源（就是静态页面）
        if not request_file_path.endswith(".py"):

            try:
                # 从html文件夹中读取出对应的文件的数据内容
                with open("./html" + request_file_path, "rb") as f:
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
        else:
            # 如果是以.py结尾的请求，那么就进行动态生成页面内容

            env = dict()  # 定义个字典，用来封装数据，然后传递到application函数中
            env["PATH_INFO"] = request_file_path  # "/login.py"

            response_boy = mini_web.application(env, self.set_status_headers)

            # 将header和body进行合并成一个整体，作为response的内容
            response_headers = "HTTP/1.1 %s\r\n" % self.status
            for header in self.headers:
                response_headers += "%s:%s\r\n" % (header[0], header[1])
            response_headers += "\r\n"

            response = response_headers + response_boy
            # 3.2 给浏览器回送对应的数据
            client_socket.send(response.encode("utf-8"))

        # 4. 关闭套接字
        client_socket.close()

    def set_status_headers(self, status, headers):
        self.status = status  # "200 OK"
        self.headers = headers  # [("Content-Type", "text/html;charset=utf-8")]

    def run(self):
        """
        用来控制整体
        :return:
        """
        while True:
            # 4. 等待客户端的链接
            client_socket, client_info = self.tcp_server_socket.accept()

            print(client_info)  # 打印 当前是哪个客户端进行了请求

            # 5. 为客户端服务
            # handle_request(client_socket)
            p = multiprocessing.Process(target=self.handle_request, args=(client_socket,))
            p.start()

            # 如果是创建了一个子进程去使用client_socket，那么子进程会复制一份这个套接字，所以要在主进程中关闭一次
            # 这样能够保证在子进程接收且调用close时，能够真正的将这个套接字关闭，如果主进程中没有close。那么即使子进程使用了close
            # 这个套接字也不会被真正的关闭，所以就不会有tcp的4次挥手
            #
            # 简单来说：如果是子进程，那么 就要在主进程中关闭一次
            #         如果是子线程，那么 就不要再主进程中关闭，因为线程的方式是共享，而进程的方式是复制
            client_socket.close()

        # 6. 关闭套接字
        self.tcp_server_socket.close()


def main():
    """
    完成整体的控制
    :return:
    """
    # 1. 创建Server服务器对象
    server = Server()

    # 2. 调用它的运行方法
    server.run()


if __name__ == '__main__':
    main()
