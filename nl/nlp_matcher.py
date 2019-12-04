from __future__ import unicode_literals, print_function

import plac
from spacy.lang.en import English
from spacy.matcher import PhraseMatcher
from spacy.tokens import Doc, Span, Token
from nl import semantics


##########################################################################

class VerbRecognizer(object):
    name = "verb_search"  # component name, will show up in the pipeline

    def __init__(self, nlp, semantic):

        label = "VERB"

        elements = semantic.get_all_values()

        self.label = nlp.vocab.strings[label]  # get entity label ID

        # Set up the PhraseMatcher – it can now take Doc objects as patterns,
        # so even if the list of companies is long, it's very efficient
        patterns = [nlp(org) for org in elements]
        self.matcher = PhraseMatcher(nlp.vocab)
        self.matcher.add("VERB", None, *patterns)

        # Register attribute on the Token. We'll be overwriting this based on
        # the matches, so we're only setting a default value, not a getter.
        Token.set_extension("has_verb", default=False)

        # Register attributes on Doc and Span via a getter that checks if one of
        # the contained tokens is set to is_tech_org == True.
        Doc.set_extension("has_verb", getter=self.has_verb)
        Span.set_extension("has_verb", getter=self.has_verb)

    def __call__(self, doc):
        """Apply the pipeline component on a Doc object and modify it if matches
        are found. Return the Doc, so it can be processed by the next component
        in the pipeline, if available.
        """
        matches = self.matcher(doc)
        spans = []  # keep the spans for later so we can merge them afterwards
        for _, start, end in matches:
            # Generate Span representing the entity & set label
            entity = Span(doc, start, end, label=self.label)
            spans.append(entity)
            # Set custom attribute on each token of the entity
            for token in entity:
                token._.set("has_verb", True)
            # Overwrite doc.ents and add entity – be careful not to replace!
            doc.ents = list(doc.ents) + [entity]
        for span in spans:
            # Iterate over all spans and merge them into one token. This is done
            # after setting the entities – otherwise, it would cause mismatched
            # indices!
            span.merge()
        return doc  # don't forget to return the Doc!

    def has_verb(self, tokens):
        return any([t._.get("has_verb") for t in tokens])


##########################################################################

class FootballPlayerRecognizer(object):
    name = "footbal_players"  # component name, will show up in the pipeline

    def __init__(self, nlp, label="PROPN"):

        companies = ["Lukaku", "Modric", "Messi", "Ronaldo"]  # etc.

        self.label = nlp.vocab.strings[label]  # get entity label ID

        # Set up the PhraseMatcher – it can now take Doc objects as patterns,
        # so even if the list of companies is long, it's very efficient
        patterns = [nlp(org) for org in companies]
        self.matcher = PhraseMatcher(nlp.vocab)
        self.matcher.add("PLAYER_NAME", None, *patterns)

        # Register attribute on the Token. We'll be overwriting this based on
        # the matches, so we're only setting a default value, not a getter.
        Token.set_extension("has_player", default=False)

        # Register attributes on Doc and Span via a getter that checks if one of
        # the contained tokens is set to is_tech_org == True.
        Doc.set_extension("has_player", getter=self.has_player)
        Span.set_extension("has_player", getter=self.has_player)

    def __call__(self, doc):
        """Apply the pipeline component on a Doc object and modify it if matches
        are found. Return the Doc, so it can be processed by the next component
        in the pipeline, if available.
        """
        matches = self.matcher(doc)
        spans = []  # keep the spans for later so we can merge them afterwards
        for _, start, end in matches:
            # Generate Span representing the entity & set label
            entity = Span(doc, start, end, label=self.label)
            spans.append(entity)
            # Set custom attribute on each token of the entity
            for token in entity:
                token._.set("has_player", True)
            # Overwrite doc.ents and add entity – be careful not to replace!
            doc.ents = list(doc.ents) + [entity]
        for span in spans:
            # Iterate over all spans and merge them into one token. This is done
            # after setting the entities – otherwise, it would cause mismatched
            # indices!
            span.merge()
        return doc  # don't forget to return the Doc!

    def has_player(self, tokens):
        """Getter for Doc and Span attributes. Returns True if one of the tokens
        is a tech org. Since the getter is only called when we access the
        attribute, we can refer to the Token's 'is_tech_org' attribute here,
        which is already set in the processing step."""
        return any([t._.get("has_player") for t in tokens])

##########################################################################
