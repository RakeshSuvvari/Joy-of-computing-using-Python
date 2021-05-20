#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 11:26:33 2021

@author: rakesh
"""
import calendar

def get_day(day_index):
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return weekdays[day_index]

def check_leap(y):
    if y%100 == 0:
        if y%400 == 0:
            return True
        else:
            return False
    else:
        if y%4 == 0:
            return True
        else:
            return False

def check_valid_date(dt,m,l):
    if l:
        if m == 2:
            if dt<=29:
                return True
            else:
                return False
        else:
            if m<8:
                if m%2 == 1:
                    if dt<=31:
                        return True
                    else:
                        return False
                else:
                    if dt<=30:
                        return True
                    else:
                        return False
            else:
                if m%2 == 0:
                    if dt<=31:
                        return True
                    else:
                        return False
                else:
                    if dt<=30:
                        return True
                    else:
                        return False
    else:
        if m == 2:
            if dt<=28:
                return True
            else:
                return False
        else:
            if m<8:
                if m%2 == 1:
                    if dt<=31:
                        return True
                    else:
                        return False
                else:
                    if dt<=30:
                        return True
                    else:
                        return False
            else:
                if m%2 == 0:
                    if dt<=31:
                        return True
                    else:
                        return False
                else:
                    if dt<=30:
                        return True
                    else:
                        return False

#main code
while(1):
    year = int(input('Enter year (1970 - ...): '))
    if year >= 1970:
        break
    else:
        print('Enter valid year')
        
while(1):
    month = int(input('Enter month (1 - 12): '))
    if month > 0 and month <= 12:
        break
    else:
        print('Enter valid month')
        

leap = check_leap(year)

while(1):
    date = int(input('Enter date: '))
    if check_valid_date(date,month,leap):
        break
    else:
        print('Enter valid date')



day_index = calendar.weekday(year,month,date)
day = get_day(day_index)
print("")
print(str(date) + '/' + str(month) + '/' + str(year),'falls on',day)
