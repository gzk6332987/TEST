from socket import *
server =  socket(AF_INET,SOCK_STREAM)

server.connect(("127.0.0.1",8888))
x = input("输入你要发送的消息>>>")
server.send(x.encode("utf-8"))

print("客户端套接字已关闭")
server.close()