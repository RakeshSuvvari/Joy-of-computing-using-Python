#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 23:23:52 2021

@author: rakesh
"""

def factorial_ite(n):
    answer = 1
    for i in range(1,n+1):
        answer = answer * i
    return answer
'''
base case or anchor case
point where recursion stops 
'''
def factorial_rec(n):
    if(n == 0):
        return 1
    if n >= 1:
        return n * factorial_rec(n-1)
    
n = int(input("Enter the +ve Number: "))
if n < 0:
    print("Factorial not defined on negtive numbers")
else:
    print("Using iterative method ",n,"! = ",factorial_ite(n))
    print("Using recursion method ",n,"! = ",factorial_rec(n))