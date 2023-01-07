import signal
import socket
from _thread import *
import time
import sys

player_ID = dict()

def signal_handler(signal, frame):
    s.close()
signal.signal(signal.SIGINT, signal_handler)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = socket.gethostname() #"172.31.25.201" "172.31.17.229"
port = 5556

server_ip = socket.gethostbyname(server)

try:
    s.bind((server,port))
except socket.error as e:
    print(str(e))

s.listen(2)
print("waiting for connection")

#currentId = "0"

def connection_send(conn, message):
    conn.send(str.encode(message))

def threaded_client(conn):
    print("Connected to: ", conn,file=sys.stderr)
    #while True:
    try:
        data = conn.recv(2048)
        #reply = data.decode('utf-8')
        if not data:
            #conn.send(str.encode("Goodbye"))
            #break
            pass
        print(f"player name: {data.decode()}",file=sys.stderr)
        player_ID[data.decode()] = conn
        print(player_ID)
        #print("reached",file=sys.stderr)
        #conn.sendall(data)
    except:
        pass
        #break

    #connection_send(conn,"Connection Closed")
    #print("Connection Closed")
    #conn.close()

while True:
    conn, addr = s.accept()
    print(addr[1])
    conn.send(str.encode(str(addr[1])))
    #print("Connected to: ", addr,file=sys.stderr)
    start_new_thread(threaded_client, (conn,))


