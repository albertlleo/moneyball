#!/usr/bin/env python3


from asr import asr
from tts import tts
import argparse
import spacy
from nl import nlp
from logic import *
from nl import nlp_context

# 0 == Google Cloud Speech
# 1 == Sphinx
# 2 == Google Speech Recognition
# ASR_MODE = 0

def main():
    parser = argparse.ArgumentParser(description='Assistant parameters')
    parser.add_argument('--asr', action='store_true')
    args = parser.parse_args()

    context = nlp_context.RequestContext()
    while context.request_is_still_active:

        input_text = ""
        if args.asr:
            input_text = asr.processASR(ASR_MODE)
        else:
            input_text = input("ask:")

        context = nlp.process(input_text, context)
        context=process_logic(context)
        context.trace()
        #query to the database of Hamit and retrieve a list with the attributes of context obecjt
        #print list and thanks blabla
        #we need more layers to improve the dialoge make it more real


    # if input_text:
    #    tts.processTextToSpeech(input_text)




if __name__ == "__main__":
    main()
