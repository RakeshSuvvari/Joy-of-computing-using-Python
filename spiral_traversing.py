#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 13:04:41 2021

@author: rakesh
"""
import turtle

turtle.bgcolor("black")
tur = turtle.Turtle() #name of a turtle
from random import randint

width = 5
height = 7
dot_distance = 25

tur.penup() # to remove printing of striaght line
list_color = ["white","yellow","brown","red","blue","green","orange","pink","violet","grey","cyan"]
tur.setpos(-250,250) #to make top left

def spiral(m, n):
    k = 0
    l = 0
    f = 0
    '''
    k = index of starting row
    l = index of starting column
    '''
    
    #tur.color("white")
    col = randint(0,10)
    tur.color(list_color[col])
    
    while(k<m and l<n):
        if (f == 1):
            tur.right(90)
        #printing the first row from remaining rows
        for i in range(l,n):
            #print(a[k][i], end=" ")
            tur.dot()
            tur.forward(dot_distance)
            
        k+=1
        f = 1
        
        tur.right(90)
        col = randint(0,10)
        tur.color(list_color[col])
        
        #printing the last colum from the remaining colum
        for i in range(k,m):
            #print(a[i][n-1], end=" ")
            tur.dot()
            tur.forward(dot_distance)
            
        n -= 1
        
        tur.right(90)
        col = randint(0,10)
        tur.color(list_color[col])
        
        if(k<m):
            #printing the last row from remaining rows 
            for i in range(n-1, l-1, -1):
               # print(a[m-1][i], end=" ")
               tur.dot()
               tur.forward(dot_distance)
               
            m -= 1
            
        tur.right(90)
        col = randint(0,10)
        tur.color(list_color[col])
        
        if(l<n):
            #printing the first column form remaining columns
            for i in range(m-1,k-1,-1):
                #print(a[i][l],end=" ")
                tur.dot()
                tur.forward(dot_distance)
            l+=1
            
            
'''a = []
count = 1
for i in range(4):
    l = []
    for j in range(4):
        l.append(count)
        count += 1
    a.append(l)'''

spiral(20,20)
turtle.done()
            