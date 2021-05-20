#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 23:08:19 2021

@author: rakesh
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver,1000)
target ='"Ramkri Bro"'
string = "Message sent using Python!! Web Automation_whatsApp"
x_args = '//span[contains(@title, '+ target + ')]'
target = wait.until(EC.presence_of_element_located((By.XPATH, x_args)))
target.click()

input_box = driver.find_element_by_class_name('_2A8P4')
for i in range(5):
    input_box.send_keys(string+Keys.ENTER)