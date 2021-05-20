#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 23:32:13 2021

@author: rakesh
"""

import numpy as np
from PIL import Image
width = 5
height = 4
array = np.zeros([height, width,3],dtype=np.uint8)
img = Image.fromarray(array)
img.save('test.png')

array1 = np.zeros([100,200,3],dtype=np.uint8)
array1[:,:100] = [255,128,0] #orange color
array1[:,100:] = [0,0,255] #blue color
img1 = Image.fromarray(array1)
img1.save('test1.png')