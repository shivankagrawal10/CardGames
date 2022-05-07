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
signal.signal(signal.SIGINT, signal_handler)
while True:
    instructions = client.receive()
    if not instructions:
        continue
    inp = int(input())
    while(inp != 0 and inp != 1 and inp != 2):
        print(f"Try Again: Enter #: 0 - Fold, 1 - Call, 2 - Raise",file=sys.stderr)
        inp = int(input())
    print("",file=sys.stderr)
    




client.close()