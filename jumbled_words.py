#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 11:04:06 2021

@author: rakesh
"""
import random
 
def choose():
    words = ['rainbow','computer','science','programming','mathematics','player','condition','reverse','water','brownine','chocolate']
    pick = random.choice(words)
    return pick

def jumble(word):
    jumbled = "".join(random.sample(word,len(word)))
    #joins the jumbled letter as word which are seperated by nothing say ""
    return jumbled

def thank(p1n,p2n,p1,p2):
    print(p1n,"Your Score is: ",p1)
    print(p2n,"Your Score is: ",p2)
    print("Thanks for playing.")
    print("Have a nice day!!")

def play():
    p1name = input("Player 1, Please Enter your name: ")
    p2name = input("Player 2, Please Enter your name: ")
    pp1 = 0 #player 1 score/points
    pp2 = 0
    turn = 0
    while(1):
        # now its computer's task
        picked_word = choose()
        #create question
        qn = jumble(picked_word)
        print("Word is: ",qn)
        #player 1
        if turn%2 == 0:
            print(p1name,"Your turn")
            ans = input("What is on your mind? ")
            if ans == picked_word:
                pp1 = pp1 + 1
                print("Your Score is: ",pp1)
            else:
                print("Bettet luck nexy time, I thought the word is: ",picked_word)
            c = int(input("Press 1 to continue or 0 to quit: "))
            if c == 0:
                thank(p1name,p2name,pp1,pp2)
                break
        
        #player 2
        else:
            print(p2name,"Your turn")
            ans = input("What is on your mind? ")
            if ans == picked_word:
                pp2 = pp2 + 1
                print("Your Score is: ",pp2)
            else:
                print("Bettet luck nexy time, I thought the word is: ",picked_word)
            c = int(input("Press 1 to continue or 0 to quit: "))
            if c == 0:
                thank(p1name,p2name,pp1,pp2)
                break
        turn = turn + 1
        

play()
            
            
            
            