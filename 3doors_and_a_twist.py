#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 12:52:42 2021

@author: rakesh
"""
import random
swap = 0 #no. of swap wins
dont_swap = 0 #no. of dont swap wins

j = 0
while(j<10):
    x = random.randint(0,2)
    #xth door will comprise of BMW
    doors = [0]*3 # array of size 3
    goatdoor = [] 
    doors[x] = "BMW"
    for i in range(0,3):
        if (i==x):
            continue
        else:
            doors[i] = "Goat"
            goatdoor.append(i)
    choice = int(input("Enter your choice as 0,1,2: "))
    door_open = random.choice(goatdoor) #open a door that comprises a Goat
    while(door_open == choice):# door open should be equal to choice made by the participant  
        door_open = random.choice(goatdoor)
    print("The door no",door_open,"has a Goat")
    ch = input("do you want to swap y/n: ")
    if ch == 'y':
        if(doors[choice] == 'Goat'):
            print("You won")
            swap += 1
        else:
            print("You Lose")
    else:
        if(doors[choice] != 'Goat'):
            print("You Won")
            dont_swap += 1
        else:
            print("You Lose")
    j += 1
#print(doors)
print(swap)
print(dont_swap)