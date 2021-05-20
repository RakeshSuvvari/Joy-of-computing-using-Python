#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 13:10:15 2021

@author: rakesh
"""

from datetime import datetime as dt
import pytz

timezones = pytz.all_timezones

for zone in timezones:
    tz = pytz.timezone(zone)
    print('current time at zone',zone,'is',dt.now(tz))