import deck
import winningHand
import matplotlib.pyplot as plt
import poker

g = poker.poker(10,100)
'''g.add_player("Shivaank")
g.add_player("SammyBoy")
g.add_player("M8")
g.add_player("YanDog")'''
num_players = 1
#num_players = int(input("Enter Number of Players: "))
agent_num = 1
#for i in range(num_players):
while True:
    name = input(f"Enter Player {num_players}'s name or \"start game\": ")
    if( name == "start game"):
        break
    if(name == "agent"):
        name += str(agent_num)
        agent_num += 1
    g.add_player(name)
    num_players += 1
for i in g.players:
    g.buy_in(i)

g.start_game()
