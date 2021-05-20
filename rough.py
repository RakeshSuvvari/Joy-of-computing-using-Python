#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 20:23:34 2021

@author: rakesh
"""

'''lower = int(input())
upper = int(input())

for num in range(lower, upper+1):
    if num>1:
        for i in range (2,num):
            if(num%i) == 0:
                break
        else:
            print(num)'''

'''m = int(input())
n = int(input())


def hcf(x,y):
    if x > y:
        smaller = y
        
    else:
       smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf

row = hcf(m,n)
print(row)'''


'''str=input()
out=''
for i in str:
    if i not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        out = out+i
    else:
        j = ord(i) + 32
        k = chr(j)
        out = out+k
print(out)'''


'''from nltk.tokenize import sent_tokenize
my_text = "Have a nice day, my friend!!! Programming in python is fun"
print(sent_tokenize(my_text))'''


import nltk
#from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords

text1 = "Welcome to programming . Programming is fun ."
text2 = " More fun is to program with Python ."
text3 = " Python is simpple yet very vast with multiple functionalities ."
text4 = " So, come enjoy programming with Python"
mytext = text1+text2+text3+text4
tokens = [t for t in mytext.split()]
sr = stopwords.words('english')
clean_tokens = tokens[:]
freq = nltk.FreqDist(tokens)
freq.plot(20, cumulative=False)




