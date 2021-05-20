#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 09:47:32 2021

@author: rakesh
"""

def binary_search(l,x,start,end):
    #Base case: 1 element
    if(end<0):
        return -1
    if start == end:
        if l[start] == x:
            return start
        else:
            return -1       
    else:
        #divide the array into two hakves
        mid = int((start+end)/2)
        if(l[mid] == x):
            return mid
        elif l[mid] > x:
            #left half
            return binary_search(l,x,start,mid-1)
        else:
            #right half
            return binary_search(l, x, mid+1, end)

l = input("Enter the elements: ").split()
for i in range(len(l)):
    l[i] = int(l[i])
#l = [20,45,60,70,90]
x = int(input("Enter element to be searched: "))
pos = binary_search(l,x,0,len(l)-1)
if pos == -1:
    print("Element",x," not found")
else:
    print("The element",x," position is: ",pos+1)