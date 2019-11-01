# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 18:46:13 2019

@author: shivank agrawal
"""

import Cards, player
class BSgame():
 def __init__(self, names):# names is a list of name
   self.__numplayers=len(names)
   self.__playerarray=[]
   self.__gamedeck = Cards.deck()
   self.__gamedeck.riffleshuffle(10)
   self. distribute(names)
   for x in range(self.__numplayers):
       print (self.__playerarray[x].getname(),self.__playerarray[x].getcardsleft())
       self.__playerarray[x].printhand()
   self.playerarray=self.__playerarray
   self.gameover = False
  

 def distribute (self,names):
   cardsdealt=0
   piles=[[] for _ in range (self.__numplayers)]
   while cardsdealt <52:
     for x in range (self.__numplayers):
       piles[x].append(self.__gamedeck.pile[cardsdealt])
       
       cardsdealt+=1
       if cardsdealt == 52:
         break
   for x in range (self.__numplayers):
     self.__playerarray.append(player.player(names[x], piles[x]))
     #piles[x].


 def gameOver(self, player):
   for player in self.__numplayers:
     if player.getcardsleft == 0:
       return True
   else:
     return False
 
    
    
    
d=Cards.deck()
a=player.player("ronald",d.pile)
a.getcardsleft()
names=["john","ron","bo"]
first = BSgame(names)
store= first.playerarray[0].playCard('5',1)
first.playerarray[0].getcardsleft