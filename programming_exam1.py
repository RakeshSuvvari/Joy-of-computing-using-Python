#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 10:10:05 2021

@author: rakesh
"""

import string

plaintext = input()
ciphertext = input()

dict = {}

for i in range(len(string.ascii_letters)):
    dict[string.ascii_letters[i]] = string.ascii_letters[(i+5)%26]

cipher=""
for i in plaintext:
  cipher += dict[i]
cipher = cipher.upper()
if sorted(list(cipher)) == sorted(list(ciphertext)):
  print("Yes",end="")
else:
  print("No",end="")