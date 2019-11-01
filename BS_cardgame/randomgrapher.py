# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 18:43:44 2019

@author: shivank agrawal
finding randomness
"""
import Cards, random_measure,time
import matplotlib.pyplot as plt
first=Cards.deck();
second=Cards.deck();
a = random_measure.randomm(first)
b=random_measure.randomm(second)
a.chronology()
a.same()
print("chronology test: ",a.chronper,"same number test: ",a.sameper)

xaxis=[];
yaxis=[];
for x in range(6):
    xaxis.append(x)
    first.riffleshuffle(x)
    a.chronology()
    a.same()
    yaxis.append((a.chronper+a.sameper)/2)
    
plt.plot(xaxis, yaxis) 
plt.show()

xaxis=[];
yaxis=[];
for x in range(6):
    xaxis.append(x)
    second.breakshuffle(x)
    b.chronology()
    b.same()
    yaxis.append((b.chronper+b .sameper)/2)
plt.plot(xaxis, yaxis) 
plt.show()
time.sleep(2)
