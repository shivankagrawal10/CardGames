# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 17:00:07 2019

@author: shivank agrawal
"""
import Cards, random_measure,time

#myprint: controls printing
run_mode="prod"
def myprint(mode, *arg):
    if (run_mode == "test"):
        print arg;
    
first=Cards.deck();
#first.reset() 
second=Cards.deck();
#second.reset  
#myprint (first.pile,"separation",second.pile)
print("successfully made decks")
time.sleep(5)
a = random_measure.randomm(first)
b= random_measure.randomm(second)
a.chronology()
a.same()
print("chronology test: ",a.chronper,"same number test: ",a.sameper)
b.chronology()
b.same()
print("chronology test: ",b.chronper,"same number test: ",b.sameper) 
#time.sleep(8)



print("Riffle shuffling")
time.sleep(2)
first.riffleshuffle(5)                   
for x in range(0,52):                    
   first.pile[x].prop()

print("Break shuffling")
time.sleep(2)
#time.sleep(5)
second.breakshuffle(5)                   
for x in range(0,52):                    
   second.pile[x].prop() # earlier when syntax was print(first.pile[x].prop()) first program was trying to print result then function
#time.sleep(5)

a.chronology()
a.same()
print("chronology test: ",a.chronper,"same number test: ",a.sameper,"avg randomness=",(a.chronper+a.sameper)/2)
b.chronology()
b.same()
print("chronology test: ",b.chronper,"same number test: ",b.sameper,"avg randomness=",(b.chronper+b.sameper)/2)          