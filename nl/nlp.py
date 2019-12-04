#!/usr/bin/env python
# coding: utf8
"""
Author: marco_bertola
"""
from __future__ import unicode_literals, print_function
import plac
from spacy.lang.en import English
from nl import nlp_matcher
from nl import semantics
from nl import nlp_context


def main():
    text = str(input("Write something:\n"))
    process(text)


def process(text):
    nlp = English()
    context = nlp_context.NlpContext()
    verb_semantic = semantics.SemanticVerb()

    players = nlp_matcher.FootballPlayerRecognizer(nlp)
    nlp.add_pipe(players, last=True)

    component = nlp_matcher.VerbRecognizer(nlp, verb_semantic)
    nlp.add_pipe(component, last=True)

    doc = nlp(text)
    print("Pipeline", nlp.pipe_names)  # pipeline contains component name
    print("Tokens", [t.text for t in doc])  # company names from the list are merged

    for token in doc:
        if token._.has_verb:
            context.has_verb = True
            context.category_verb = verb_semantic.category(token)

    context.trace()

    # for token in doc:
    #    print(token.lemma_)
    # print("Entities", [(e.text, e.label_) for e in doc.ents])  # all orgs are entities


if __name__ == "__main__":
    main()
