# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 18:56:17 2019

@author: shivank agrawal
"""
#import Cards
class player:
   def __init__(self, name='', hand=[]):
       self.__name = name #player's name
       self.__hand = hand #list of cards in player's hand
       
   def playCard(self,cardface,numcards):
       '''
       returns an arrays of cards played and removes those cards from deck
       if cards not in pile then variable return value -1
       if number of cards player selecter to play are greater than number of those cards he/she has then empty returned
       '''
       counter=0
       cardlocation=[], played=[]
       for checker in len(self.__hand):
           if cardface == self.__hand[checker]:
               counter+=1
               cardlocation.append(checker)
       if numcards<=counter:
           for num in numcards:
               played.append(self.__hand[cardlocation[num]])
               self.__hand.remove(cardlocation[num])
       elif counter==0:
           played=-1
       return played
   
   #def callBS():
   def getname(self):
       return self.__name
   def getcardsleft(self):
       return len(self.__hand)
   def printhand (self):
       for x in range(len(self.__hand)):
           self.__hand[x].prop()