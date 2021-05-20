#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 16:28:46 2021

@author: rakesh
"""

def magic_square(n):
    magicSquare = []
    for i in range(n):
        l = []
        for j in range(n):
            l.append(0)
        magicSquare.append(l)
    
    p = n//2
    q = n-1
    
    num = n*n
    count = 1
    
    while(count<=num):
        if(p == -1 and q == n):
            p = 0
            q = n-2
        else:
            if(q == n):
                q = 0
            if(p < 0):
                p = n-1
                
        if(magicSquare[p][q] != 0):
            p = p+1
            q = q-2
            continue
        else:
            magicSquare[p][q] = count
            count += 1
            
        p = p-1
        q = q+1
    
        
    for i in range(n):
        for j in range(n):
            print(magicSquare[i][j], end=" ")
        print()
    print("The sum of elements in each row/column/diagonal is: ",n*((n**2)+1)/2)
magic_square(3)