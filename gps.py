#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 14:28:35 2021

@author: rakesh
"""

'''import csv
with open('route.csv','r') as f:
    handler = csv.reader(f)
    
    for row in handler:
        lat = float(row[0])
        long = float(row[1])
        print(lat)
        print(long)
        print(lat+long)'''
        
from gmplot import gmplot
import  csv

gmap = gmplot.GoogleMapPlotter(28.689169, 77.324448, 17)
gmap.coloricon = "https://www.googlemapsmakers.com/v1/%s/"

with open('route.csv','r') as f:
    handler = csv.reader(f)
    k = 0
    
    for row in handler:
        lat = float(row[0])
        long = float(row[1])
        
        if(k == 0):
            gmap.marker(lat,long,'green')
            k = 1
        else:
            gmap.marker(lat,long,'blue')

gmap.marker(lat,long,'red')

gmap.draw("mymap.html")
    