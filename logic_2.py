#!/usr/bin/env python3

from logic import *
from nl import nlp_context
from asr import asr
import argparse
import random


def process_logic(context):
    do_logic(context)
    return context


def say_something(text):
    print(text)


def select_question(dialogues):
    # select rows
    rows = dialogues[(dialogues.iloc[:, 0] == 1)
                     & (dialogues.iloc[:, 1] == 1)
                     & (dialogues.iloc[:, 2] == 1)
                     & (dialogues.iloc[:, 3] == 1)
                     & (dialogues.iloc[:, 4] == 1)]
    rows = rows.iloc[random.randint(0, rows.shape[0] - 1)]
    return rows.dialogue


def edit_dialogue(player):
    dialogues = pd.read_csv('dialogue.csv')
    for column in player:
        if player[0] == 1:
            dialogues.iloc[0:3, 0].replace(1, 0, inplace=True)
        if player[1] == 1:
            dialogues.iloc[3:6, 1].replace(1, 0, inplace=True)
        if player[2] == 1:
            dialogues.iloc[6:9, 2].replace(1, 0, inplace=True)
        if player[3] == 1:
            dialogues.iloc[9:12, 3].replace(1, 0, inplace=True)
        if player[4] == 1:
            dialogues.iloc[12:15, 4].replace(1, 0, inplace=True)
    return dialogues


def do_logic(context):
    # budget = 0
    # intent = "buy"
    # position = ""
    # feature = ""
    # duration = ""
    # cost = 0
    player = [0, 0, 0, 0, 0]
    # Check if the user input say us any information of it
    if context.has_verb is True:
        player[0] = 1
    if context.has_budget is True:
        player[1] = 1
    if context.has_attribute is True:
        player[2] = 1
    if context.has_quantifier is True:
        player[3] = 1
    # if context.has_player is True:
    #    print("counter for player name is +1")
    #    player[3] = True
    #    counter += 1
    if context.has_player_role is True:
        player[4] = 1

    while context.request_is_still_active is True and all(i == 1 for i in player) is False:

        context.trace()
        print("list", player)
        # If intent is general, actualize the input to an specific one
        # pick a random question
        dialogues = edit_dialogue(player=player)
        bot_response = select_question(dialogues=dialogues)
        input(bot_response)
        context = nlp.process(bot_response, context)
        do_logic(context)
    return context


def main():
    parser = argparse.ArgumentParser(description='Assistant parameters')
    parser.add_argument('--asr', action='store_true')
    args = parser.parse_args()
    context = nlp_context.RequestContext()
    while context.request_is_still_active:

        input_text = ""
        if args.asr:
            input_text = asr.processASR(ASR_MODE)
        else:
            input_text = input("How can I help?\n")

        context = nlp.process(input_text, context)
        context = process_logic(context)
        context.trace()
        # query to the database of Hamit and retrieve a list with the attributes of context obecjt
        # print list and thanks blabla
        # we need more layers to improve the dialoge make it more real

    # if input_text:
    #    tts.processTextToSpeech(input_text)


if __name__ == "__main__":
    main()
