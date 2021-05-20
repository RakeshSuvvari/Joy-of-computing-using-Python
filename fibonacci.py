#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 10:37:11 2021

@author: rakesh
"""
'''
    0th fib no = 0 #base case
    1st fib no = 1
    
    2nd fib no = 0+1 = 1
    3rd fib no = 1+1 = 2
    4th fib no = 1+2 = 3
    5th fib no = 2+3 = 5
'''
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Enter the value n: "))
if n < 0:
    print("Fibonacci sequence is not defined for negative numbers")
else:
    print("Fibonacci number at position",n,"is",fibonacci(n))

