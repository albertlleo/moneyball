#!/usr/bin/env python
# coding: utf8
"""
Author: marco_bertola
"""


class RequestContext:
    has_verb = False
    category_verb = ""

    has_attribute = False
    category_attribute = ""

    has_quantifier = False
    quantifier_attribute = ""

    has_player = False
    category_player = ""

    has_player_role = False
    category_player_role = ""

    def trace(self):
        print("\n******CONTEXT******")
        print("has_verb\t", self.has_verb)
        print("category_verb\t", self.category_verb)
        print("has_attribute\t", self.has_attribute)
        print("category_attribute\t", self.category_attribute)
        print("has_quantifier\t", self.has_quantifier)
        print("quantifier_attribute\t", self.quantifier_attribute)
        print("has_player\t", self.has_player)
        print("category_player\t", self.category_player)
        print("has_player_role\t", self.has_player_role)
        print("category_player_role\t", self.category_player_role)
        print("************")