#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 13:22:57 2021

@author: rakesh
"""

import imageio
from PIL import Image
import  numpy as np
import random

img = imageio.imread("map-01.jpg")
count_pun = 0
count_in = 0
count = 0
while(count <= 100000):
    x = random.randint(0,1271-1)
    y = random.randint(0,1300-1)
    z = 0
    
    if(img[x][y][z] == 255):
        count_in += 1
        count += 1
    else:
        if(img[x][y][z] == 254):
            count_pun += 1
            count += 1

area_pun = (count_pun/count_in) * 3287263
print(area_pun)
    