#encoding = utf-8
import socket
import select
import Queue

server = ("192.168.1.4", 20000)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#费阻塞方式
sock.setblocking(False)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


sock.bind(server)
sock.listen(5)
#conn, address = sock.accept()

rLists = [sock]
wLists = []
msg_que = {}
timeout = 20

while rLists:
    rs, ws, es = select.select(rLists, wLists, rLists, timeout)
    if not (rs or ws or es):
        print "timeout..."
        break
    for s in rs:
        if s is sock:
            conn, address = s.accept()
            print "connectde by ", address
            conn.setblocking(False)
            rLists.append(conn)
            msg_que[conn] = Queue.Queue()
        else:
            data = s.recv(1024)
            if data:
                print data
                msg_que[s].put(data)
                if s not in wLists:
                    wLists.append(s)
            else:
                if s in wLists:
                    wLists.remove(s)
                rLists.remove(s)
                s.close()
                del msg_que[s]
                
    for s in ws:
        try:
            msg = msg_que[s].get_nowait()
        except Queue.Empty:
            print "msg empty"
            wLists.remove(s)
        else:
            s.send(msg)
            
    for s in es:
        print "except ", s.getpeername()
        rLists.remove(s)
        wLists.remove(s)
        s.close()
        del msg_que[s]