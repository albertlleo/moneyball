# -*- coding: utf-8 -*-
"""
Created 2019

@author: Albert Lleó
"""

# The Natural Language Toolkit: https://www.nltk.org/
# This toolkit is a standard for linguistic processing of text data -- you will 
# probably work with it in the introductory course on computational linguistics in the second term. 

# If you don't have it, install it with the following command 
# in the Terminal (Mac, Linux) or Anaconda prompt (Windows):
# conda install -c anaconda nltk
import nltk
# *** we use the NLTK's pre-implemented functions for accessing WordNet ***
from nltk.corpus import wordnet as wn

### *** Possible error: ***

#LookupError: 
#**********************************************************************
#  Resource wordnet not found.
#  Please use the NLTK Downloader to obtain the resource:
#
#import nltk
#nltk.download('wordnet')

### this means that, although you have installed NLTK, you don't 
### have the wordnet resource yet.
### *** solution: *** 
## do what the message tells you, in the console:
#import nltk
#nltk.download('wordnet')


def synset (word_list, category):
    related_words = {}
    for word in word_list:
        all_synsets = wn.synsets(word, category)
        for synset in all_synsets:
            if word not in related_words.keys():
                related_words[word]=synset.lemma_names()
    return related_words



#### IF we want we can improve the code and add a revision of the hypernames

# all_synsets = wn.synsets('find','v')
# first_synset = all_synsets[0]
# print(first_synset)
# print()
#
# hypernyms_list=first_synset.hypernym_paths() # ATTENTION! this is a list of list, because each synset can have more than one hypernym.
# In this case, the list has only one element
# hypernyms = hypernyms_list[0] # we take the first (and only) hypernym path of this synset
# print('AAAa')
# print(hypernyms_list)




#IF we need to examine 2 words, for instance

# for word in ["find", "search"]:
#   print(word)
#   synsets = wn.synsets(word, 'v')
#   for synset in synsets:
#       print("\tsynset:", synset)
#       print()





## We can use somth like this, import a file
def load_word_list(filename = "key_words.txt"):
    with open(filename, 'r') as file:
        data = file.readlines()
    data = [x.strip() for x in data]
    return data

# #get list of categories
# def load_catogory_list(filename = "categories_battig.txt"):
#     with open(filename, 'r') as file:
#         data = file.readlines()
#     data = [x.strip() for x in data]
#     return data





### Dont look at this by now:

#define the judgment function
# def category_judgment(word_list, category_list):
#     f = open("wordnet_categorisation.txt","w+")
#     for word in word_list:
#         all_synsets = wn.synsets(word,'n')
#         first_synset = all_synsets[0]
#         hypernyms_list = first_synset.hypernym_paths()
#         hypernyms = hypernyms_list[0]
#         for category in category_list:
#             for hyp_synset in hypernyms:
#                 lemmas_hypernym = hyp_synset.lemma_names()
#                 for lemma in lemmas_hypernym:
#                     if lemma == category:
#                         f.write(word + '\t' + category + '\n')
#     f.close()
#     print('The output file, according to the needs of the currently assignment, is created as wordnet_categorisation.txt.')
                    



word_list = load_word_list()
# print(word_list)
words_related=synset(word_list,'v')
print(words_related)

