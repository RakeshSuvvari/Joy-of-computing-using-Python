#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 14:51:47 2021

@author: rakesh
"""

import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.downloader.download('vader_lexicon')
file = 'data_file.xlsx'
xl=pd.ExcelFile(file) #read the excel file
dfs = xl.parse(xl.sheet_names[0])#parsing  Excel sheet to data frame
dfs = list(dfs['Timeline'])#removes blank rows from the data frame
print(dfs)
sid=SentimentIntensityAnalyzer()
str1 = "UTC+5:30"
for data in dfs:
    a = data.find(str1)
    if(a==-1):
        # has not found str1
        ss = sid.polarity_scores(data)
        print(data)
        for k in ss:
            print(k,ss[k])
        
