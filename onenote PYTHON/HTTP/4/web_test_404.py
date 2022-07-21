from socket import *
import re
import time


def main(ip, port):
    tcp_server = socket(AF_INET, SOCK_STREAM)
    tcp_server.bind((ip, port))
    tcp_server.listen(10)

    while True:

        try:
            new_socket, addr = tcp_server.accept()
            recv = new_socket.recv(1024).decode("utf-8")
            print(recv)
            recv_line = recv.splitlines()[0]

        except:
            print("无法获取套接字!!!")
            time.sleep(1)
            continue

        try:
            after_re = re.match("\w+ (/.*)[ ]", recv_line).group(1)
            get = after_re
            print("get到的信息:", after_re, "\n")
        except:
            response_head = "HTTP/1.1 404 file not found\r\n\r\n"
            response_body = "file not found!"
            new_socket.send(response_head.encode("utf-8"))
            new_socket.send(response_body.encode("utf-8"))
            continue

        if get == "/":
            request_file_path = "./index.html"
        else:
            request_file_path = "." + get

        try:
            f = open(request_file_path, "rb")
            response_head = "HTTP/1.1 200 OK\r\n\r\n"
            response_body = f.read()
            print(response_body.decode("utf-8"))
            new_socket.send(response_head.encode("utf-8"))
            new_socket.send(response_body)
            time.sleep(1)

        except:  # 404
            response_head = "HTTP/1.1 404 file not found\r\n\r\n"
            response_body = "file not found!"
            new_socket.send(response_head.encode("utf-8"))
            new_socket.send(response_body.encode("utf-8"))
            time.sleep(2)
        else:
            new_socket.close()
            continue


if __name__ == "__main__":
    main(ip="127.0.0.1", port=8765)
