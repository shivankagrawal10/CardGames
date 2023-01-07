"""
Server Side

@author: shivank agrawal
Runner for server and game logic
"""

from re import S

from sympy import false
import threaded_poker
import network as ntwk

import socket
from _thread import *
import time
import sys
import signal

player_thread = dict()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = socket.gethostname() #"172.31.17.229"
port = 5556

server_ip = socket.gethostbyname(server)

try:
    s.bind((server,port))
except socket.error as e:
    print(str(e))

s.listen(2)
#s.setblocking(False)
print("Waiting for connection")

g = threaded_poker.poker(10,100)
#currentId = "0"
capPlayers = int(input("Enter Number of Players: "))
numPlayers = 0
numPlayersLock = allocate_lock()

def signal_handler(signal, frame):
    print("Server Connection Closed")
    s.close()
    # close the socket here
    sys.exit(0)

def threaded_client(conn,addr):
    print("Connected to: ", conn,file=sys.stderr)
    try:
        #getting player name
        data = conn.recv(2048)
        #reply = data.decode('utf-8')
        if not data:
            pass
        name = data.decode()
        print(f"Adding {name} to the game",file=sys.stderr)
        succesAdd = g.add_player(name,conn,addr)
        if(succesAdd==0):
            conn.sendall(b"You have been added to the game\n")
            conn.sendall(b"Wait for game to start . . .\n")
        else:
            conn.sendall(b"You have not been added, try again with a different name")
        g.show_players()
    except:
        print("did not add to game")
        print("Connection Closed")
        conn.close()
    
    x=0
    while(g.isPlaying(name)):
        x += 1

    print(f"{name} Connection Closed")
    conn.close()
    

signal.signal(signal.SIGINT, signal_handler)

#This is a daemon thread to keep adding players to the game as they connect
def create_client():
    global numPlayers
    while numPlayers < capPlayers:
        conn, addr = s.accept()
        conn.send(str.encode(str(addr[1])))
        #print("reached",file=sys.stderr)
        #print("Connected to: ", addr,file=sys.stderr)
        player_thread[addr] = start_new_thread(threaded_client, (conn,addr))
        numPlayersLock.acquire()
        numPlayers += 1
        numPlayersLock.release()
    
    '''while True:
        conn, addr = s.accept()
        conn.send(str.encode(str(-1)))
    '''

start_new_thread(create_client, ())
#startGame = False
startGame = bool(input("Enter 1 when ready to play\n"))
g.start_game()
print("finished")
print("Server Connection Closed")
s.close()
# close the socket here
sys.exit(0)

