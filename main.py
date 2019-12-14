#!/usr/bin/env python3


from asr import asr
import argparse
from logic import *
from nl import nlp_context
from nl.nlp import *
#from NFI import filter

# 0 == Google Cloud Speech
# 1 == Sphinx
# 2 == Google Speech Recognition
ASR_MODE = 0


def main():
    parser = argparse.ArgumentParser(description='Assistant parameters')
    parser.add_argument('--asr', action='store_true')
    args = parser.parse_args()

    context = nlp_context.RequestContext()
    nlp_engine = Nlp()

    while context.request_is_still_active:

        input_text = ""
        if args.asr:
            input_text = asr.processASR(ASR_MODE)
        else:
            input_text = input("ask:")

        context = nlp_engine.process(input_text, context)
        context.trace()
        context = process_logic(context)

    #filter(context)


if __name__ == "__main__":
    main()
