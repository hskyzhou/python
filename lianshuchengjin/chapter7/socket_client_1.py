import socket

server = ("192.168.1.4", 20000)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(server)

sock.send("hello")

data = sock.recv(1024)
print " echo ", data
sock.close()