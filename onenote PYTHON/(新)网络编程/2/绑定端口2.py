from socket import *
udp_socket = socket(AF_INET,SOCK_DGRAM)
local_addr = ('',6668)


s = udp_socket.bind(local_addr)


recv_date = udp_socket.recvfrom(1024)
print(recv_date[0].decode('gbk'))
print(recv_date[1])

udp_socket.close()