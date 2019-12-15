#!/usr/bin/env python
# coding: utf8
"""
Author: marco_bertola
"""


class RequestContext:

    request_is_still_active = True
    request_did_success = False
    request_is_the_first_one = False

    has_verb = False
    category_verb = ""

    has_attribute = False
    category_attribute = ""

    has_quantifier = False
    quantifier_attribute = ""

    has_player_role = False
    category_player_role = ""

    has_budget = False
    budget_amount = 0

    has_player_name = False
    player_name = ""

    has_confirmation = False
    category_confirmation = ""

    def trace(self):
        print("\n******CONTEXT******")
        print("has_verb\t", self.has_verb)
        print("category_verb\t", self.category_verb)
        print("has_attribute\t", self.has_attribute)
        print("category_attribute\t", self.category_attribute)
        print("has_quantifier\t", self.has_quantifier)
        print("quantifier_attribute\t", self.quantifier_attribute)
        print("has_player_role\t", self.has_player_role)
        print("category_player_role\t", self.category_player_role)
        print("has_budget\t", self.has_budget)
        print("budget_amount\t", self.budget_amount)
        print("has_player_name\t", self.has_player_name)
        print("player_name\t", self.player_name)
        print("request_is_still_active\t", self.request_is_still_active)
        print("request_did_success\t", self.request_did_success)
        print("has_confirmation\t", self.has_confirmation)
        print("confirmation_category\t", self.category_confirmation)
        print("************")

