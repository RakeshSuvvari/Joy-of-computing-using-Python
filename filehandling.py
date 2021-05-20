#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 15:30:33 2021

@author: rakesh
"""
import random

def evolve(x):
    ind = random.randint(0,len(x)-1)
    p = random.randint(1,100)

    #print(p)
    if(p == 1):
        lst.append(ind)
        if(x[ind] == '0'):
            x[ind] = '1'
        else:
            x[ind] = '0'
        

with open("DNA_text.txt","r+") as myfile:
    x = myfile.read()
    x = list(x) 
    #print(len(x))
    
lst = [] #global declaration
for i in range(0,10000):
    evolve(x)

print(lst)
print(x)