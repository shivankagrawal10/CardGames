# -*- coding: utf-8 -*-
"""
Copied from BS_CardGame Folder
Making Card class better
Ended up rewriting entire class

@author: shivank agrawal
card class defines individual card objects given numeric specification
deck class creates a full 52 deck of cards and has breakshuffle and riffle shuffle capabilities
"""
import random
import time
#print("Starting import random_measure")
#import random_measure
#print("Ending import random_measure")

Ref_Num = list(map(str,list(range(2,11)))) + ["J","Q","K","A"]
Ref_Suite = ["Spades", "Clubs", "Diamonds", "Hearts"]
class card:
    def __init__(self, number, suite):
        self.number = number
        self.suite = suite
    def __str__(self):
        s = f"{Ref_Num[self.number]} {Ref_Suite[self.suite]}"
        return s

class deck:        
        def __init__ (self):    #Constructor - automatically creates standard deck
            self.pile=[]
            for suite in range(0,4):
                for number in range(0,13):
                    self.pile.append(card(number,suite))
        def __str__(self):
            s=''
            for i in range(13):
                for j in range(4):
                    s += self.pile[i*4+j].__str__().ljust(15)
                s += "\n" 
            return s
        
        def breakshuffle (self,times):
            for x in range(times):  
                cardspulled=random.randint(10,26)
                where=random.randint(0,51-cardspulled)
                temp=[]
                for takeout in range(0,cardspulled):
                    temp.append(self.pile.pop(where))
                for putin in range(0,cardspulled):
                    self.pile.insert(putin,temp[putin])
                    
        def riffleshuffle (self,times):
           
            for x in range(times):  
                cardspulled=random.randint(20,31)
                where=random.randint(0,1)*(52-cardspulled)
                temp=[]
                for takeout in range(cardspulled):
                    temp.append(self.pile.pop(where))
                numcards=0
                lastplace=0
                while numcards<cardspulled:
                    if cardspulled <5:
                        pulled=random.randint(0,(cardspulled-numcards))
                    else:
                        pulled=random.randint(0,5)
                    if pulled+lastplace > 51:
                        pulled=51-lastplace
                    for numput in range(0,pulled):
                        self.pile.insert(lastplace,temp[numcards+numput])
                        lastplace=lastplace+1
                    numcards=numcards+pulled
                    lastplace=lastplace+pulled+random.randint(0,5)
                    if lastplace>=51-cardspulled:
                        lastplace=51-(cardspulled-numcards)

