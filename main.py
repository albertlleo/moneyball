#!/usr/bin/env python3


from asr import asr
from tts import tts
import argparse
import spacy



# 0 == Google Cloud Speech
# 1 == Sphinx
# 2 == Google Speech Recognition
ASR_MODE = 0


def main():

    parser = argparse.ArgumentParser(description='Assistant parameters')
    parser.add_argument('--asr', action='store_true')
    args = parser.parse_args()

    input_text = ""
    if args.asr :
        input_text = asr.processASR(ASR_MODE)
    else :
        input_text = input("ask:")
    
    if input_text:
        tts.processTextToSpeech(input_text)

    nlp = spacy.load('en')
    doc = nlp(input_text)
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
