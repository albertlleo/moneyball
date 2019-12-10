#!/usr/bin/env python
# coding: utf8
"""
Author: marco_bertola
"""


class Semantic:

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
                        print(node)
                    else:
                        synonymous = [node]
                        semantic[parent] = synonymous
                last_line = self.__recurse_tree(node, tabs + 1, source, semantic)

        return last_line


class SemanticVerb(Semantic):
    semantics = {}

    def __init__(self):
        self._build_tree(open("nl/voc/verb.voc"))


class SemanticPlayerAttribute(Semantic):
    semantics = {}

    def __init__(self):
        self._build_tree(open("nl/voc/playerAttribute.voc"))


class SemanticAttributeQuantifier(Semantic):
    semantics = {}

    def __init__(self):
        self._build_tree(open("nl/voc/attributeQuantifier.voc"))


class SemanticPlayerRole(Semantic):
    semantics = {}

    def __init__(self):
        self._build_tree(open("nl/voc/playerRole.voc"))
