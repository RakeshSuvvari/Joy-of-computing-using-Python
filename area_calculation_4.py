#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 15:29:26 2021

@author: rakesh
"""

from PIL import Image
import random
im = Image.open("map-01.jpg")
rgb_im = im.convert("RGB")
count_in = 0
count_pun = 0
count = 0
while(count <= 100000):
    x = random.randint(0,1300-1)
    y = random.randint(0,1271-1)
    
    z = 0
    r,g,b = rgb_im.getpixel((x,y))
    if(r==255 and g==255 and b==255):
        count_in += 1
        count += 1
    elif(r == 254 and g==0 and b==0):
        count_pun += 1
        count += 1

area_pun = (count_pun/count_in) * 3287263
print(area_pun)