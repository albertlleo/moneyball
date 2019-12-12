#!/usr/bin/env python3


from asr import asr
from tts import tts
import argparse
import spacy
from nl import nlp
from logic import *

# 0 == Google Cloud Speech
# 1 == Sphinx
# 2 == Google Speech Recognition
ASR_MODE = 0


def main():
    parser = argparse.ArgumentParser(description='Assistant parameters')
    parser.add_argument('--asr', action='store_true')
    args = parser.parse_args()

    input_text = ""
    if args.asr:
        input_text = asr.processASR(ASR_MODE)
    else:
        input_text = input("ask:")

    # if input_text:
    #    tts.processTextToSpeech(input_text)

    context = nlp.process(input_text)
    process_logic(context)


if __name__ == "__main__":
    main()
