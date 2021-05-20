#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 09:43:21 2021

@author: rakesh
"""
from PIL import Image
import random
end = 100

def show_board():
    img = Image.open("slb.jpg")
    img.show()

def check_ladder(points):
    if points == 1:
        print("Ladder")
        return 38
    elif points == 4:
        print("Ladder")
        return 14
    elif points == 9:
        print("Ladder")
        return 31
    elif points == 21:
        print("Ladder")
        return 42
    elif points == 28:
        print("Ladder")
        return 84
    elif points == 51:
        print("Ladder")
        return 67
    elif points == 71:
        print("Ladder")
        return 91
    elif points == 80:
        print("Ladder")
        return 100
    else:
        # Not a ladder
        return points
    
def check_snake(points):
    if points == 17:
        print("Snake")
        return 7
    elif points == 54:
        print("Snake")
        return 34
    elif points == 62:
        print("Snake")
        return 19
    elif points == 64:
        print("Snake")
        return 60
    elif points == 87:
        print("Snake")
        return 24
    elif points == 93:
        print("Snake")
        return 73
    elif points == 95:
        print("Snake")
        return 75
    elif points == 98:
        print("Snake")
        return 79
    else:
        # Not a snake
        return points
    
def reached_end(points):
    if points == end:
        return True
    else:
        return False
    
def play():
    #input player1 name
    p1_name = input("Player1, Please Enter your name: ")
    #input player2 name
    p2_name = input("Player2, Please Enter your name: ")
    #initial points of player1
    pp1 = 0
    #initial points of player2
    pp2 = 0
    
    turn = 0
    while(1):
        if turn%2 == 0:
            #player 1 turn
            print("\n",p1_name,"your turn")
            #ask player's choice to continue
            c = int(input("press 1 to continue, 0 to quit "))
            if c == 0:
                print(p1_name," scored", pp1)
                print(p2_name," scored", pp2)
                print("Quiting the game..., Thanks for playing!")
                break
            #generate a random number from 1,2,3,4,5,6
            dice = random.randint(1,6)
            print("Dice showed: ", dice)
            #add the points
            pp1 = pp1 + dice
            pp1 = check_ladder(pp1)
            pp1 = check_snake(pp1)
            if pp1 > end:
                pp1 = pp1-dice #need to wait for exact points to reach fixed final point
            print(p1_name,"Your score",pp1)
            
            if reached_end(pp1):
                print(p1_name,' won')
                break
        else:
            #player 2 turn
            print("\n",p2_name,"your turn")
            #ask player's choice to continue
            c = int(input("press 1 to continue, 0 to quit "))
            if c == 0:
                print(p1_name," scored", pp1)
                print(p2_name," scored", pp2)
                print("Quiting the game..., Thanks for playing!")
                break
            #generate a random number from 1,2,3,4,5,6
            dice = random.randint(1,6)
            print("Dice showed ",dice)
            #add the points
            pp2 = pp2 + dice
            pp2 = check_ladder(pp2)
            pp2 = check_snake(pp2)
            if pp2 > end:
                pp2 = pp2-dice #need to wait for exact points to reach fixed final point
            print(p2_name,"Your score",pp2)
            
            if reached_end(pp2):
                print(p2_name,' won')
                break
        turn += 1

#show_board()
play()