#!/usr/bin/env python
# coding: utf8
"""
Author: marco_bertola
"""
from __future__ import unicode_literals, print_function
import plac
from spacy.lang.en import English
from spacy.matcher import PhraseMatcher
from spacy.tokens import Doc, Span, Token
from nlp_matcher import *
from semantics import *


def main():
    # For simplicity, we start off with only the blank English Language class
    # and no model or pre-defined pipeline loaded.
    nlp = English()
    text = str(input("Write something:\n"))

    verb = SemanticVerb()
    verb.trace()

    players = FootballPlayerRecognizer(nlp)
    nlp.add_pipe(players, last=True)

    component = VerbBuyRecognizer(nlp)
    nlp.add_pipe(component, last=True)

    component = VerbSearchRecognizer(nlp)
    nlp.add_pipe(component, last=True)

    doc = nlp(text)
    print("Pipeline", nlp.pipe_names)  # pipeline contains component name
    print("Tokens", [t.text for t in doc])  # company names from the list are merged
    print("Doc has_player", doc._.has_player)  # Doc contains tech orgs
    print("Doc buy_player", doc._.buy_player)  # Doc contains tech orgs
    for token in doc:
        print("Token has_player", token._.has_player)
        print("Token has_player", token._.has_player)
        print("Token has_player", token._.has_player)

    for token in doc:
        print(token.lemma_)

    print("Entities", [(e.text, e.label_) for e in doc.ents])  # all orgs are entities


if __name__ == "__main__":
    main()
