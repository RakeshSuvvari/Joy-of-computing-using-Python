#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 12:56:23 2021

@author: rakesh
"""

import random
import matplotlib.pyplot as plt

account = 0 #details of my gain or loss
x = []
y = []

for i in range(365):
    x.append(i+1)
    bet = random.randint(1,10)
    lucky_draw = random.randint(1,10)
    #print("Your number is:",bet)
    #print("Your lucky draw number is:",lucky_draw)
    
    # I need keep amount 100/- if i won i will get 900
    # or i will loose my 100/-
    
    if bet == lucky_draw:
        account = account + 900 - 100 # which gives my net gain/loss
    else:
        account = account-100
        
    y.append(account)
    
print("Amount in my game account",account)
plt.plot(x,y)
plt.show()
