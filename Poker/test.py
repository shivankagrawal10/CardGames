import deck
import winningHand
import matplotlib.pyplot as plt
import player

g = player.poker(10,100)
g.add_player("Shivaank")
g.add_player("SammyBoy")
g.add_player("M8")
g.add_player("YanDog")

for i in g.players:
    g.buy_in(i)

g.show_players()
g.start_round()
g.show_players()

'''d = deck.deck()
#print(d)
win_freq = dict()
for i in range(9):
    win_freq[i] = 0
num_sim = 5*10**3
for i in range(num_sim):
    #Shuffle Deck
    for i in range(10):
        d.riffleshuffle(1)

    #Check top 7 cards
    check = winningHand.checker(d.pile[0:7])
    win_freq[max(0,check.check()-1)]+=1

for i in win_freq:
    win_freq[i] = round(win_freq[i]/num_sim,2)
print(win_freq)

ziplist = list(zip(list(win_freq.keys()),list(win_freq.values())))
print(ziplist)


plt.bar(*zip(*win_freq.items()))
plt.show()'''