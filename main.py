#!/usr/bin/env python3


from asr import asr
from tts import tts
import spacy





def main():

    #speech = asr.processASR()
    #if speech:
    #    tts.processTextToSpeech(speech)

	nlp = spacy.load('en')
	doc = nlp("Next week I'll   be in Madrid.")
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
