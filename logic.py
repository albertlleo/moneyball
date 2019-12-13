#!/usr/bin/env python3


from nl import *
import sqlite3
from nl import nlp
import pandas as pd
import random


def process_logic(context):
    do_logic(context)
    return context


def saySomething(text):
    print(text)


def do_logic(context):
    dialogues = pd.read_csv('dialogue.csv')
    counter = 0
    # budget = 0
    # intent = "buy"
    # position = ""
    # feature = ""
    # duration = ""
    # cost = 0

    print("initial counter:", counter)
    # Check if the user input say us any information of it
    if context.has_verb is True:
        print("counter for verb is +1")
        counter += 1
    if context.has_attribute is True:
        print("counter for attribute is +1")

        counter += 1
    if context.has_quantifier is True:
        print("counter for quantifier is +1")

        counter += 1
    if context.has_player is True:
        print("counter for player name is +1")

        counter += 1
    if context.has_player_role is True:
        print("counter for role is +1")

        counter += 1
    if context.has_budget is True:
        print("counter for budget is +1")

        counter += 1

    print("counter after first check:", counter)
    context.trace()

    while context.request_is_still_active is True:
        # If intent is general, actualize the input to an specific one
        if context.has_verb is True:
            if context.category_verb == "find" or context.category_verb == "buy":
                saySomething("")

                while counter != 5:

                    if context.has_player is True:
                        print("Ok, lets find the price for ", context.category_player)
                        # retrieve price and all from player context.category_player
                        counter = 5

                    if context.has_budget is False:
                        # input_text = input("random output from our database on this side asking the budget. Okey, what's your budget?:")
                        row = dialogues[(dialogues['has_verb'] == 1) & (dialogues['has_budget'] == 0)]
                        row = row.iloc[random.randint(0, row.shape[0] - 1)]
                        # make numbers understandable and then change
                        context.budget_amount = input(row.dialogue)  # nlp.process(input_text, context)
                        context.has_budget = True
                        context.trace()
                        print("Counter is:", counter)
                        counter += 1

                    if context.has_attribute is False:
                        row = dialogues[(dialogues.has_verb == 1) & (dialogues.has_budget == 1) & (dialogues.has_attribute == 0)]
                        row = row.iloc[random.randint(0, row.shape[0] - 1)]
                        input_text = input(row.dialogue)
                        context = nlp.process(input_text, context)
                        context.has_attribute = True
                        context.trace()
                        counter += 1

                    if context.has_quantifier is False:
                        row = dialogues[
                            (dialogues.has_verb == 1) & (dialogues.has_budget == 1) & (dialogues.has_attribute == 1) & (dialogues.has_quantifier == 0)]
                        row = row.iloc[random.randint(0, row.shape[0] - 1)]
                        # input_text = input("random output from our database on this side asking the budget. Okey, what'?:")
                        # context.quantifier_attribute = input("Perfect, let's move on. You want a good or a regular player? Note that the price would change")  # pick up random sentences from a database
                        input_text = input(row.dialogue)
                        context = nlp.process(input_text, context)
                        context.has_quantifier = True
                        context.trace()

                        counter += 1

                    if context.has_player_role is False:
                        # input_text = input("random output from our database on this side asking the budget. Okey, what'?:")
                        # context.category_player_role = input("Nice, let's move on. What role would like to have your player? striker, defender, medium...")  # pick up random sentences from a database
                        row = dialogues[
                            (dialogues.has_verb == 1) & (dialogues.has_budget == 1) & (dialogues.has_attribute == 1) & (
                                        dialogues.has_quantifier == 1) & (dialogues.has_player_role == 0)]
                        row = row.iloc[random.randint(0, row.shape[0] - 1)]
                        input_text = input(row.dialogue)
                        context = nlp.process(input_text, context)
                        context.has_player_role = True
                        context.trace()

                        counter += 1

                    print("Final counter;", counter)

            else:
                saySomething("plis at first do only find or buy, later we will add more actions.")
                do_logic(context)

        else:
            print("define a verb")
            do_logic(context)

        context.request_is_still_active = False
        return context
