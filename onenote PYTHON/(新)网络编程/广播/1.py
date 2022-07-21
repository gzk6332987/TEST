import socket

# 1. 创建UDP套接字
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 2. DongTai WEB. 设置UDP套接字允许其广播(注意如果udp套接字需要广播，则一定要添加此语句)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# 选做 绑定本地信息
# s.bind(("", 8080))

# 4. 向本局域网中发送广播数据
# 此时只要是本局域网中的电脑上有 用1060端口的udp程序 它就会收到此数据
dest_info = ("<broadcast>", 1060)  # <broadcast>会自动改为本局域网的广播ip
s.sendto('hello world !'.encode('utf-8'), dest_info)

# 5. 关闭套接字
s.close()
