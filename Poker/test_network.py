import poker
import network as ntwk

import socket
from _thread import *
import time
import sys
import signal

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

g = poker.poker(10,100)
#currentId = "0"

def signal_handler(signal, frame):
    print("Server Connection Closed")
    s.close()
    # close the socket here
    sys.exit(0)

def threaded_client(conn):
    print("Connected to: ", conn,file=sys.stderr)
    try:
        data = conn.recv(2048)
        #reply = data.decode('utf-8')
        if not data:
            pass
        name = data.decode()
        print(f"Adding {name} to the game",file=sys.stderr)
        g.add_player(name)
        conn.sendall(b"You have been added to the game")
    except:
        print("did not add to game")
        print("Connection Closed")
        conn.close()
    
    print("Connection Closed")
    conn.close()
    

signal.signal(signal.SIGINT, signal_handler)
while True:
    conn, addr = s.accept()
    conn.send(str.encode(str(addr[1])))
    #print("Connected to: ", addr,file=sys.stderr)
    start_new_thread(threaded_client, (conn,))




