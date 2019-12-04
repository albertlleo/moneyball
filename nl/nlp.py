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


def debug_log(doc):
    for token in doc:
        print("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}".format(
            token.text,
            token.idx,
            token.lemma_,
            token.is_punct,
            token.is_space,
            token.shape_,
            token.pos_,
            token.tag_
        ))
    print("Entities", [(e.text, e.label_) for e in doc.ents])


def main():
    text = str(input("Write something:\n"))
    process(text)


def process(text):
    nlp = English()
    context = nlp_context.NlpContext()

    verb_semantic = semantics.SemanticVerb()
    component = nlp_matcher.VerbRecognizer(nlp, verb_semantic)
    nlp.add_pipe(component, last=True)

    attribute_semantic = semantics.SemanticPlayerAttribute()
    component_attribute = nlp_matcher.PlayerAttributeRecognizer(nlp, attribute_semantic)
    nlp.add_pipe(component_attribute, last=True)

    doc = nlp(text)
    print("Pipeline", nlp.pipe_names)  # pipeline contains component name
    print("Tokens", [t.text for t in doc])  # company names from the list are merged

    for token in doc:
        if token._.has_verb:
            context.has_verb = True
            context.category_verb = verb_semantic.category(token)
        if token._.has_attribute:
            context.has_attribute = True
            context.category_attribute = attribute_semantic.category(token)

    context.trace()

    #debug_log(doc)


if __name__ == "__main__":
    main()
