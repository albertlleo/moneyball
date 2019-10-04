
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 283 20:23:46 2019

@author: Albert Lleo, Hamit, ...
"""


# Playwiser

#We need to create a script-dialoge? or just with an example written we are done?

import sys

print('Hi, wellcome to Playwiser! My name is Sussan and I will become your personal assistant on this search.')
name = input("What's your name? ")
print("Nice to meet you coach " + name + "!")
answer1= input("Are you here to search for a player (search) or just to ask some habilities (habilities) of a player?")
if answer1 is "search":
	position = input("Alriht. Let's start defining the first position player you want. Is it DFC, MC or DL ") #guys its just supercoding, we need to define evttng and correct syntax lol
	if position is "DFC":
		print ("Alright, you need a" + position + "with more speed or with more strength?")
		print("...")

	elif position is "MC":
		print ("Alright, you need a" + position + "with more speed. with more strength or vision?")
		print("...")
	
	else:
		print ("Alright, you need a" + position + "with more speed, with more strength or more precision?")
		print("...")



print("Alright " + name + " let's do ths sht (dude im just testing git desktop this is not official)")
