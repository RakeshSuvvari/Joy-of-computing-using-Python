#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 18:28:43 2021

@author: rakesh
"""

def linear_search(n,x):    
    element = []
    for i in range(1,n):
        element.append(i)
    
    flag = 0
    for i in element:
        if(i==x):
            print("Yes! I found my number at position: "+str(i))
            flag = 1
            break
    
    if(flag == 0):
        print("Number is not found")