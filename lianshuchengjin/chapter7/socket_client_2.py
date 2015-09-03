#encoding=utf-8
import socket
import time
server = ("192.168.1.4", 20000)
msg = ["heollo", "hskyzhou", "xueer", "dongfangbubai"]

socks = []
#创建10个客户端
for i in range(10):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socks.append(sock)
#对于每一个客户端，请求连接服务端
for s in socks:
    s.connect(server)

counter = 0

for m in msg:
    for s in socks:
        s.send("%d send %s" % (counter, m))
        counter += 1
        
    for s in socks:
        data = s.recv(1024)
        print "%s echo %s" % (s.getpeername(), data)
sock.close()