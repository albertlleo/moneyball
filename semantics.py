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


class Semantic:
    semantics = {}

    def trace(self):
        print(self.semantics)

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
                        print(parent + node)
                last_line = self.__recurse_tree(node, tabs + 1, source, semantic)

        return last_line


class SemanticVerb(Semantic):

    def __init__(self):
        self._build_tree(open("voc/verb.voc"))
