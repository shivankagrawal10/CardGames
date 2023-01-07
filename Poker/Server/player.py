"""
Internal datastructure - individual player record

@author: shivank agrawal

"""

import network as ntwk
class player:
    def __init__(self,name):
        self.name = name
        self.cards = []
        self.money = 0
        self.curr_bet = 0                                   #Particular round bet ()
        self.game_bet = 0                                   #Sum of all rounds bet (1 full game of 5 cards)
        #self.net = ntwk.Network()
    
    def set_money(self,money):                              #To only be accessed by game program
        self.money = money
    
    def set_cards(self,cards):
        self.cards = cards
    
    def bet(self,amount):
        self.money -= amount
        self.curr_bet += amount
        return amount

    def fold(self):
        temp = self.cards
        self.cards = []
        return temp

    def player_value(self):
        return f"{self.name.ljust(10)} - ${self.money}" 

    def __str__(self):
        if(self.cards):
            return f"{self.name.ljust(10)} - {self.cards[0].__str__().ljust(10)}, {self.cards[1].__str__().ljust(11)} - ${self.money}"
        else:
            return f"{self.name.ljust(10)} - No Cards - ${self.money}"

