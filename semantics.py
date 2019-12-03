#!/usr/bin/env python
# coding: utf8
"""
Author: marco_bertola
"""


class NlpContext:
    has_verb = False
    category_verb = ""

    has_attribute = False
    category_attribute = ""

    has_player = False
    category_player = ""

    def trace(self):
        print("\n******CONTEXT******")
        print("has_verb\t", self.has_verb)
        print("category_verb\t", self.category_verb)
        print("has_attribute\t", self.has_attribute)
        print("category_attribute\t", self.category_attribute)
        print("has_player\t", self.has_player)
        print("category_player\t", self.category_player)
        print("************")


class Semantic:
    semantics = {}

    def category(self, token):

        for key, value in self.semantics.items():
            if str(token) in value:
                return key
        return ""

    def trace(self):
        print(self.semantics)

    def get_all_values(self):

        elements = []
        for items in self.semantics.values():
            for item in items:
                elements.append(item)
        return elements

    def _build_tree(self, file):
        self.__recurse_tree(None, 0, file, self.semantics)

    def __recurse_tree(self, parent, depth, source, semantic):

        last_line = source.readline().rstrip()
        while last_line:
            tabs = last_line.count('\t')
            if tabs < depth:
                break
            node = last_line.strip()
            if tabs >= depth:
                if parent is not None:
                    if parent in semantic.keys():
                        semantic[parent].append(node)
                    else:
                        synonymous = [node]
                        semantic[parent] = synonymous
                last_line = self.__recurse_tree(node, tabs + 1, source, semantic)

        return last_line


class SemanticVerb(Semantic):

    def __init__(self):
        self._build_tree(open("voc/verb.voc"))
