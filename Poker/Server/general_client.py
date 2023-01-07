"""
Client side

@author: shivank agrawal
Prompts user (human or agent) for game action
"""

import player
import network as ntwk
import signal, sys
from Agents import Random_Agent

AgentArr = []

client = ntwk.Network()

def signal_handler(signal, frame):
    #print("Client Connection Closed")
    client.close()
    # close the socket here
    sys.exit(0)

if(client.id<0):
    print("Max players already on Server")
    sys.exit(0)

isAgent = True
type_of_player = input("Enter Player or Agent")
name = 0
if(type_of_player == "Player"):
    isAgent = False
    name = input("Enter Player Name (do not make it a self standing #): ")
    #curr_state = player.player(name)
    client.send(name)
if(type_of_player == "A"):
    name = input("Enter Agent #")
    client.send(name)
    name = int(name)
    #if(name == 0):
    Agent = Random_Agent.Agent()

print(client.receive())
#print(client.receive())
signal.signal(signal.SIGINT, signal_handler)
amt = 0
while True:
    instructions = client.receive()
    if not instructions:
        break
    else:
        print(instructions,end="",file=sys.stderr)
    if(instructions == "Enter #: 0 - Fold, 1 - Call, 2 - Raise\n"):
        if(isAgent == False):
            inp = int(input())
        else:
            inp = int(Agent.getDecision())
        while(inp != 0 and inp != 1 and inp != 2):
            print(f"Try Again: Enter #: 0 - Fold, 1 - Call, 2 - Raise",file=sys.stderr)
            inp = int(input())
        print(str(inp))
        client.send(str(inp))
        if(inp == 2):
            while True:
                try:
                    if(isAgent == False):
                        amt = int(input("Enter Amount To Bet:"))
                    else:
                        amt = int(Agent.getRaise(20))
                    amt_send = "|"+str(amt)
                    client.send(amt_send)
                    print(amt)
                except:
                    print("Enter a valid amount",file=sys.stderr)
                    continue  
                break         

        
        print("",file=sys.stderr)
    




client.close()