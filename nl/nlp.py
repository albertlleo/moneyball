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

DEBUG = True


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
    context = nlp_context.RequestContext()

    verb_semantic = semantics.SemanticVerb()
    matcher_verb = nlp_matcher.VerbRecognizer(nlp, verb_semantic)
    nlp.add_pipe(matcher_verb, last=True)

    attribute_semantic = semantics.SemanticPlayerAttribute()
    matcher_attribute = nlp_matcher.PlayerAttributeRecognizer(nlp, attribute_semantic)
    nlp.add_pipe(matcher_attribute, last=True)

    quantifier_semantic = semantics.SemanticAttributeQuantifier()
    matcher_quantifier = nlp_matcher.AttributeQuantifierRecognizer(nlp, quantifier_semantic)
    nlp.add_pipe(matcher_quantifier, last=True)

    player_role_semantic = semantics.SemanticPlayerRole()
    matcher_player_role = nlp_matcher.PlayerRoleRecognizer(nlp, player_role_semantic)
    nlp.add_pipe(matcher_player_role, last=True)

    doc = nlp(text)
    print("Pipeline", nlp.pipe_names)  # pipeline contains component name
    print("Tokens", [t.text for t in doc])  # company names from the list are merged

    for token in doc:
        matcher_verb.match(token, context, verb_semantic)
        matcher_attribute.match(token, context, attribute_semantic)
        matcher_quantifier.match(token, context, quantifier_semantic)
        matcher_player_role.match(token, context, player_role_semantic)

    if DEBUG:
        debug_log(doc)
        #context.trace()

    return context


if __name__ == "__main__":
    main()
