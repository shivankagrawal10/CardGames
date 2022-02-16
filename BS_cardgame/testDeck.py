# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 15:43:28 2019

@author: shivank agrawal
"""

import Cards

playerdeck = Cards.deck()

for x in range(52): # goes from 0 to 51
    playerdeck.pile[x].prop()

playerdeck.riffleshuffle(10)    
print("\n after shuffle")
for x in range(52): # goes from 0 to 51
    playerdeck.pile[x].prop()