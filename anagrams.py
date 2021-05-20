#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 22:34:21 2021

@author: rakesh
"""

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

if(sorted(str1)==sorted(str2)):
    print("These are Anagrams")
else:
    print("These are not Anagrams")