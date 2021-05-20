#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 16:31:40 2021

@author: rakesh
"""

#Image enhancement CLAHE
#CLAHE - Contrast Limited Adapptive Histogram Equalisation
# we are going to used histogram equalisation
import cv2

# read the image
img = cv2.imread('bullet_shots.jpeg')

#preparation for CLAHE
clahe = cv2.createCLAHE()

#convert the color img to gray sacle img
#so this enchancement technique works well

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Applay enhancement
enh_img = clahe.apply(gray_img)

#save it to a file
cv2.imwrite('bullet_shots_enhanced.jpeg',enh_img)

print("Done Enchancing")