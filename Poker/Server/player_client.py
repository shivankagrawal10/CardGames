"""
Client side - if player is a human

@author: shivank agrawal
Prompts user to take action during game round (system in)
"""

import player
import network as ntwk
import signal, sys

client = ntwk.Network()

def signal_handler(signal, frame):
    #print("Client Connection Closed")
    client.close()
    # close the socket here
    sys.exit(0)

if(client.id<0):
    print("Max players already on Server")
    sys.exit(0)

name = input("Enter Player Name: ")
#curr_state = player.player(name)
client.send(name)

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
        inp = int(input())
        while(inp != 0 and inp != 1 and inp != 2):
            print(f"Try Again: Enter #: 0 - Fold, 1 - Call, 2 - Raise",file=sys.stderr)
            inp = int(input())
        client.send(str(inp))
        if(inp == 2):
            while True:
                try:
                    amt = int(input("Enter Amount To Bet:"))
                    client.send(str(amt))
                    break
                except:
                    print("Enter a valid amount",file=sys.stderr)
                    continue    
        

        
        print("",file=sys.stderr)
    




client.close()