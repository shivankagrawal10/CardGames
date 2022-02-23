import socket
from _thread import *
import time
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = socket.gethostname() #"172.31.17.229"
port = 5556

server_ip = socket.gethostbyname(server)

try:
    s.bind((server,port))
except socket.error as e:
    print(str(e))

s.listen(2)
print("waiting for connection")

#currentId = "0"

def threaded_client(conn):
    print("Connected to: ", conn,file=sys.stderr)
    while True:
        try:
            data = conn.recv(2048)
            #reply = data.decode('utf-8')
            if not data:
                #conn.send(str.encode("Goodbye"))
                break
            print(f"player name: {str.encode(data)}",file=sys.stderr)
            print("reached",file=sys.stderr)
            #conn.sendall(data)
        except:
            break

    print("Connection Closed")
    conn.close()

while True:
    conn, addr = s.accept()
    #print("Connected to: ", addr,file=sys.stderr)
    start_new_thread(threaded_client, (conn,))


