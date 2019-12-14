#!/usr/bin/env python3
from dialogs.dialogs import *
from nl import *
from nl import nlp
import random


def process_logic(context):
    do_logic(context)
    return context


def saySomething(text):
    print(text)


def select_player():
    name_player = input("Select one player of the list to be the elected:")
    return name_player


def say_goodbye():
    saySomething("Thanks for using playwiser, until the next time")
    return


def is_only_verb(context):
    pass


def has_verb_and_player(context):
    return context.has_verb and context.has_player_name


def no_verb(context):
    return context.has_verb == False


def not_has_budget(context):
    return context.has_budget == False


def only_verb(context):
    return context.has_verb \
           and not context.has_attribute \
           and not context.has_player_role \
           and not context.has_quantifier \
           and not context.has_budget \
           and not context.has_player_name


def find_request_is_ready(context):
    return context.has_verb \
           and context.has_attribute \
           and context.has_player_role \
           and context.has_quantifier \
           and context.has_budget \
           and context.category_verb == "find"


def do_logic(context):
    context.trace()

    dialog = DialogManager()

    if True:
        # If intent is general, actualize the input to an specific one

        if no_verb(context):
            dialog.processDialog(ID_NO_VERB)
            return context

        if only_verb(context):
            dialog.processDialog(ID_WELCOME)

        if has_verb_and_player(context):
            dialog.processDialog(ID_FIND_HAS_PLAYER_NAME, [context.player_name])
            return context

        if not_has_budget(context):
            context.budget_amount = input("Please, type your budget")
            context.has_budget = True

        if context.has_player_role is False:
            dialog.processDialog(ID_ASK_PLAYER_ROLE)
            return context

        if context.has_attribute is False:
            dialog.processDialog(ID_ASK_ATTRIBUTE, [context.category_player_role])
            return context

        if context.has_quantifier is False:
            dialog.processDialog(ID_ASK_QUANTIFIER, [context.category_attribute, context.category_player_role])
            return context

        if find_request_is_ready(context):
            dialog.processDialog(ID_FIND_REQUEST_IS_READY, [context.category_player_role, context.quantifier_attribute, context.category_attribute])
            context.request_is_still_active = False


