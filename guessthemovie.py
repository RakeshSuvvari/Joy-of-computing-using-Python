#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 23:25:47 2021

@author: rakesh
"""
import random

movies=["avatar","matrix","avengers","deadpool","source code","jungle book","triangle","fight club","inception","johnwick"]

def create_question(movie):
    n = len(movie)
    letters = list(movie)
    temp_lst = []
    for i in range(n):
        if letters[i]==" ":
            temp_lst.append(" ")
        else:
            temp_lst.append("*")
    qn =''.join(str(x) for x in temp_lst)
    return qn

def is_present(letter, picked_movie):
    count = picked_movie.count(letter)
    if count == 0:
        return False
    else:
        return True
    
def unlock(qn, movie, letter):
    ref_lst = list(movie)
    qn_lst = list(qn)
    temp_lst = []
    n = len(movie)
    for i in range(n):
        if ref_lst[i] == " " or ref_lst[i] == letter:
            temp_lst.append(ref_lst[i])
        else:
            if qn_lst[i] == "*":
                temp_lst.append("*")
            else:
                temp_lst.append(ref_lst[i])
    
    qn_new =''.join(str(x) for x in temp_lst)
    return qn_new

def play():
    p1name = input("Enter the name of Player1: ")
    p2name = input("Enter the name of Player2: ")
    pp1 = 0
    pp2 = 0
    turn = 0
    willing = True
    while willing:
        if turn%2 == 0:
            #player1
            print(p1name,"Your turn")
            picked_movie = random.choice(movies)
            qn = create_question(picked_movie)
            print(qn)
            modified_qn = qn
            not_said = True
            while(not_said):
                letter = input("Your letter: ")
                if(is_present(letter, picked_movie)):
                    #unlock
                    modified_qn = unlock(modified_qn, picked_movie, letter)
                    print(modified_qn)
                    d = int(input("press 1 to guess the movie or 2 to unlock another letter: "))
                    if d == 1:
                        ans = input("Your answer: ")
                        if ans == picked_movie:
                            pp1 = pp1+1
                            print("Your are Correct")
                            not_said = False
                            print(p2name, "Your Score: ",pp1)
                        else:
                            print("Wrong answer, Try again.")
                    else:
                        continue
                                            
                else:
                    print(letter,"Not Found")
                    
            c = int(input("Press 1 to continue or 0 to Quit: "))
            if c == 0:
                print(p1name, "Your Score: ",pp1)
                print(p2name, "Your Score: ",pp2)
                print("Thanks for playing")
                print("Have a nice day")
                willing = False
                
        else:
            #player2
            print(p2name,"Your turn")
            picked_movie = random.choice(movies)
            qn = create_question(picked_movie)
            print(qn)
            modified_qn = qn
            not_said = True
            while(not_said):
                letter = input("Your letter: ")
                if(is_present(letter, picked_movie)):
                    #unlock
                    modified_qn = unlock(modified_qn, picked_movie,letter)
                    print(modified_qn)
                    d = int(input("press 1 to guess the movie or 2 to unlock another letter: "))
                    if d == 1:
                        ans = input("Your answer: ")
                        if ans == picked_movie:
                            pp2 = pp2+1
                            print("Your are Correct")
                            not_said = False
                            print(p1name, "Your Score: ",pp2)
                        else:
                            print("Wrong answer, Try again.")
                    else:
                        continue
                                            
                else:
                    print(letter,"Not Found")
            c = int(input("Press 1 to continue or 0 to Quit: "))
            if c == 0:
                print(p1name, "Your Score: ",pp1)
                print(p2name, "Your Score: ",pp2)
                print("Thanks for playing")
                print("Have a nice day")
                willing = False
                
        turn = turn + 1
                    
                        

play()