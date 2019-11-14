#!/usr/bin/env python3


from asr import asr
from tts import tts
import spacy



# 0 == Google Cloud Speech
# 1 == Sphinx
# 2 == Google Speech Recognition
ASR_MODE = 0


def main():

    speech = asr.processASR(ASR_MODE)
    if speech:
        tts.processTextToSpeech(speech)

    nlp = spacy.load('en')
    doc = nlp(speech)
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

    


if __name__ == "__main__":
    main()
