import player
import network as ntwk

client = ntwk.Network()

name = input("Enter Player Name: ")
#curr_state = player.player(name)

client.send(name)

print(client.receive())