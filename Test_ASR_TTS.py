#!/usr/bin/env python3


from asr import asr
from tts import tts


def main():

    speech = asr.processASR()
    if speech:
        tts.processTextToSpeech(speech)


if __name__ == "__main__":
    main()
