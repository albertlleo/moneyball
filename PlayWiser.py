#!/usr/bin/python
"""
Created on Thu Oct 283 20:23:46 2019

@author: Albert Lleo, Hamit, ...
"""


# Playwiser

#We need to create a script-dialoge? or just with an example written we are done?

import sys

#def selection(answer1):
    

def search():
	position = input("Alriht. Let's start defining the first position player you want. Is it DFC, MC or DL:  ") #guys its just supercoding, we need to define evttng and correct syntax lol
	if position == "DFC":
		char =  input("Alright, you need a " + position + "with more speed or with more strength?")
		print("...")

	elif position == "MC":
		char =  input("Alright, you need a " + position + " with more speed. with more strength or vision?")
		print("...")
        
	elif position == "DL":
		char =  input("Alright, you need a " + position + " with more speed, with more strength or more precision?")
		print("...")
    
#    else:
#        print("Please choose a correct POS")
#        search()
        


def printPlayer(x):

	#print players vector, array, list.... idk
	print("the caractheristics of" + player + "are ......") #printPLayer(player)
#    return(player)
    
    
print('Hi, wellcome to Playwiser! My name is Sussan and I will become your personal assistant on this search.')
name = input("What's your name? ")
print("Nice to meet you coach " + name + "!")
answer1= input("Are you here to search for a player (search) or just to ask some habilities (habilities) of a player?")


#we should put all this in a function up there and here jsut put selection(answer1) and/or try this of try and except, im starting on python sorry guys
if answer1 == "search":
	search()
    
elif answer1 == "habilities":
	player = input("Tell us the player you want to obtain features: ")
	printPlayer(player)

else:
    print("please enter a valid answer")




