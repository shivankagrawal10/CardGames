#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 11:11:54 2019

@author: 3004910
"""

"Bubble Sort"
import matplotlib.pyplot as plt;
oldTime=1;
numentry=100
SizeArr= [None]*numentry;# number of entries
Time=[None]*numentry;

for y in range(1,numentry):
    size = 10*y;
    Arr = [None]*size;
    SizeArr[y-1]=size
    print(size);
    import random;
    i= len(Arr);
    for x in range(size):
        Arr[x]=i;
        i-=1;
    checker = True;
    numchanges = 0;
    import time;
    start = time. time()
    while (checker == True):
        for x in range (len(Arr)-1):
            if (Arr[x]>Arr[x+1]):
                temp=Arr[x];
                Arr[x]=Arr[x+1];
                Arr[x+1]=temp;
                numchanges = numchanges+1;
                
        if (numchanges==0):
                checker=False;
            
               
        numchanges=0;
        
    end = time. time();
    Time [y-1]=end-start; " Size is x, time [y] is y var"    
    print ("For run with 10^", y, " size=", size, " time=", end-start, "% increase=", (end-start)/oldTime);
    print ("First 10 values=>");
    for x in range (0,5):            
        print (Arr[x]);
    oldTime=(end-start)
    "print(end - start);"
    time.sleep(1);
    
# plotting the points  
plt.plot(SizeArr, Time) 
  
# naming the x axis 
plt.xlabel('Array Size') 
# naming the y axis 
plt.ylabel('Time Took') 
  
# giving a title to my graph 
plt.title('My first graph!') 
  
# function to show the plot 
plt.show()             