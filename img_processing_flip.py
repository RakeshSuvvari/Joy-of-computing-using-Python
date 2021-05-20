#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 15:53:51 2021

@author: rakesh
"""


#Fliping the image

from PIL import Image

# opening the image
img = Image.open("evidence_board.jpg")

#transposing
transposed_img = img.transpose(Image.FLIP_LEFT_RIGHT)

# save it to a human understandable format
transposed_img.save('evidence_board_1.jpg')
print("Done flipping")

