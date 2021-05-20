#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 11:31:17 2021

@author: rakesh
"""

def remove_matching_letter(l1, l2):
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i] == l2[j]:
                c = l1[i]
                l1.remove(c)
                l2.remove(c)
                l = l1+['*']+l2
                return[l,True]
    l = l1+['*']+l2
    return[l,False]


p1name = input("Enter player 1 name: ")
p1name = p1name.lower()# convert to lower case
p1name = p1name.replace(" ","") # if spaces btw the words remove them
p2name = input("Enter player 2 name: ")
p2name = p2name.lower()
p2name = p2name.replace(" ","")

l1 = list(p1name)
l2 = list(p2name)

proceed = True
while proceed:
    ret_list = remove_matching_letter(l1, l2)
    con_list = ret_list[0]
    proceed = ret_list[1]
    star_index = con_list.index('*')
    l1 = con_list[:star_index]
    l2 = con_list[star_index+1:]

count = len(l1) + len(l2)

result = ['Friends', 'Love', 'Affection', 'Marriage', 'Enemy', 'Siblings']

while len(result)>1:
    split_index = (count%len(result))-1
    if split_index >= 0:
        right = result[split_index+1:]
        left = result[:split_index]
        result = right + left
    else:
        result = result[:len(result)-1]
        
print(result[0])
