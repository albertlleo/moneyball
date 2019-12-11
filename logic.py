#!/usr/bin/env python3


from nl import *
import sqlite3




counter=0
budget=0
intent="buy"
position=""
feature=""
duration=""
cost=0
end="False"

#Check if the user input say us any information of it
if budget!=0:
    counter+=1
if position!="":
    counter+=1
if feature!="":
    counter+=1

while end is not "True":
# If intent is general, actualize the input to an specific one
    if intent is "general":
        print("Great!  You prefer to buy or to rent a player?")
        intent=input()

    if intent is "buy":
        connection = sqlite3.connect("players.db")
        cursor = connection.cursor()

        while(counter!=3):

            if budget==0:
                print("(random output from our database on this side asking the budget. Okey, what's your budget?")
                budget = float(input())
                cursor.execute("SELECT DISTINCT Value FROM players WHERE Value<budget")
                print("For this budget, you have this players.:")
                result = cursor.fetchall()
                for r in result:
                    print(r)

                counter+=1

            if position == "":
                print("(random output from our database on this side asking the position. Nice, what's your position? Just to clarify my research")
                position = input()
                cursor.execute("SELECT DISTINCT Position FROM players WHERE Position=position ")
                print("For this Position, you have this players.:")
                result = cursor.fetchall()
                for r in result:
                    print(r)
                counter+=1

            if feature == "":
                print("(random output from our database on this side asking the position. Fine! what's your best feature to have? Just to clarify my research")
                position = input()
                cursor.execute("SELECT DISTINCT Feature FROM players WHERE Feature=feature ")
                print("For this Position, you have this players.:")
                result = cursor.fetchall()
                for r in result:
                    print(r)
                counter += 1

        print("My results with those specifications are:")
        cursor.execute("SELECT all FROM players WHERE Budget<budget and Position=position and Feature=feature ")
        print("For this data, you have this players.:")
        players = cursor.fetchall()
        for r in players:
            print(r)

        cursor.close()
        connection.close()
        end="True"


    if intent is "rent":
        connection = sqlite3.connect("players.db")
        cursor = connection.cursor()

        while (counter != 4):
            if budget==0:
                print("(random output from our database on this side asking the budget. Okey, what's your budget?")
                budget = float(input())
                cursor.execute("SELECT DISTINCT Value FROM players WHERE Value<budget")
                print("For this budget, you have this players.:")
                result = cursor.fetchall()
                for r in result:
                    print(r)

                counter+=1

            if duration == "":
                print("(random output from our database on this side asking the position. Nice, what's the duration? Just to clarify my research")
                duration = input()
                counter+=1


            if position == "":
                print("(random output from our database on this side asking the position. Nice, what's your position? Just to clarify my research")
                position = input()
                cursor.execute("SELECT DISTINCT Position FROM players WHERE Position=position ")
                print("For this Position, you have this players.:")
                result = cursor.fetchall()
                for r in result:
                    print(r)
                counter+=1


            if feature == "":
                print(
                    "(random output from our database on this side asking the position. Fine! what's your best feature to have? Just to clarify my research")
                position = input()
                cursor.execute("SELECT DISTINCT Feature FROM players WHERE Feature=feature ")
                print("For this Position, you have this players.:")
                result = cursor.fetchall()
                for r in result:
                    print(r)
                counter += 1

        cursor.execute("SELECT DISTINCT Cost FROM players WHERE Budget<budget and Position=position and Feature=feature ")

        # and duration???

        print("For this data, you have this players.:")
        players = cursor.fetchall()

        for r in players:
            print(r)

        cursor.close()
        connection.close()
        intent=="end"

