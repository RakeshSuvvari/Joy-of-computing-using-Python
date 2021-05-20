#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 18:39:16 2021

@author: rakesh
"""
def binary_search(a,x):
    start = 0
    end = len(a)-1
    flag = 0 # 0 means element has not found yet
    count = 0
    while(start <= end and flag == 0):
        count += 1
        mid = (start+end)//2
        if(x==a[mid]):
            flag = 1
            print("The element is found at position "+str(mid))
            print("No. iterations are: "+str(count))
            return
        else:
            if(x<a[mid]):
                end = mid-1
            else:
                start = mid+1

    print("The number is not present")
            
a = []
for i in range(1,10001):
    a.append(i)

binary_search(a,10000)
    
