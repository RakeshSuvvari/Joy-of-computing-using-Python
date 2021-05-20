#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 20 13:27:05 2021

@author: rakesh
"""

def checkNum(num):
    iterations = 1
    while(num!=1):
        if(num%2 == 0):
            num = num//2
            iterations += 1
        else:
            num = (3*num) + 1
            iterations += 1
    print(iterations)

checkNum(26)
            