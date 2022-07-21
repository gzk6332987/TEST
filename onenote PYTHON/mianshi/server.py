from socket import *
server =  socket(AF_INET,SOCK_STREAM)

server.bind(("127.0.0.1",8888))
print("等待client连接......")
server.listen(10)

a,b = server.accept()
msg = a.recv(1024)

print(f"client的ip为 {b[0]} 端口为{b[1]} 发送的消息为 " + msg.decode("utf-8"))

a.close()
print("监听已关闭")

server.close()
print("套接字已关闭...")