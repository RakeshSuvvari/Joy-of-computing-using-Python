#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 12:25:47 2021

@author: rakesh
"""

from PIL import Image
im = Image.open('test1.png')
rgb_im = im.convert('RGB')
r, g, b = rgb_im.getpixel((150,1))
print(r,g,b)