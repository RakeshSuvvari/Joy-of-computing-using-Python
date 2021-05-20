#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 11:12:16 2021

@author: rakesh
"""

import speech_recognition as sr

AUDIO_FILE = ("sample2.wav")
# use audio file as source

r = sr.Recognizer() # initialize the recognizer

with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)
    #reads the audio file
try:
    print("audio file contains "+r.recognize_google(audio))
except sr.UnkownValueError:
    print("Google Speech Recognition could not understand the audio")
except sr.RequestError:
    print("couldn't get the result from Google Speech Recognition")