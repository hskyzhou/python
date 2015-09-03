#encoding=utf-8
import socket

server = ('192.168.1.4', 20000)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(server)
sock.listen(5)
conn, address = sock.accept()  #阻塞方式
print "connect by ", address
while True:
    data = conn.recv(1024)
    if not data:
        break
    print data
    conn.send(data)
sock.close()