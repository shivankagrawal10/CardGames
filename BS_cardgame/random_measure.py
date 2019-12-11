# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 13:25:26 2019

@author: shivank agrawal
Finding randomness of a deck of cards
    -check chronology (48 - sum of occurancce/48)
    -check like numbers together (39 - sum of occurance/39)
    -check chronology of suites
    
    lessons learned: cannot import from a file and import this file to that one
    do testing in seperate file
"""
#import Cards
import time

#time.sleep(1);

class randomm:
    #chroncounter=0
    def __init__ (self, inDeck):
        self.deck=inDeck;
        #print("received List->", inDeck.pile)
        time.sleep(1)
       #self.deck.pile=list
    def chronology(self): # measures how close to chronology the deck is
        self.chroncounter=0
        for x in range(51):
            if self.deck.pile[x].Number==self.deck.pile[x+1].Number-1:
                #print (self.deck.pile[x].Number," ",self.deck.pile[x+1].Number-1)
                self.chroncounter+=1    
        self.chronper = ((48 - self.chroncounter)/(48.0)) *100
    def same(self): #measures how closely cards of same number are together
        self.samecounter=0
        for x in range(51):
            if self.deck.pile[x].Number==self.deck.pile[x+1].Number:
                #print (self.deck.pile[x].Number," ",self.deck.pile[x+1].Number-1)
                self.samecounter+=1    
        self.sameper = ((39 - self.samecounter)/(39.0)) *100
#myDeck = Cards.deck()

