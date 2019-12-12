#!/usr/bin/env python3


import pyttsx3
import os


def processTextToSpeech(text):

    if os.name == 'nt':
        engine = pyttsx3.init("sapi5", debug=False)
    else:
        engine = pyttsx3.init("nsss", debug=False)
    engine.say(text)
    engine.runAndWait()


def main():
    processTextToSpeech("test")


if __name__ == "__main__":
    main()
