# -*- coding: utf-8 -*-

"""This is the entry point of the program."""

from .languages import LANGUAGES
from collections import defaultdict

'''
# First pancake version:

def detect_language(text, languages):
    """Returns the detected language of given text."""
    spanish = 0
    german = 0
    english = 0
    txt_lst = text.split()
    for word in txt_lst:
        if word in LANGUAGES[0]['common_words']:
            spanish += 1
        elif word in LANGUAGES[1]['common_words']:
            german += 1
        elif word in LANGUAGES[2]['common_words']:
            english += 1

    if spanish > (german and english):
        return "Spanish"
    elif german > (spanish and english):
        return "German"
    elif english > (spanish and german):
        return "English"
'''


def detect_language(text, languages):
    """Returns the detected language of given text."""
    
    # Create a dictionary to store the count of words per language in the text:
    lang_count = defaultdict(int)
    
    # Transforming the text string into a list of strings and iterating through each word:
    for word in text.split():
        
        # Iterating through each language dictionary in LANGUAGES:
        for lang in LANGUAGES:
            
            # Checking if the word in lowercase is present in the list of common words of each language:
            if word.lower() in lang['common_words']:
                
                # If it is, then add 1 to the count of that language:
                lang_count[lang['name']] += 1

    # From the lang_count dictionary, return the key with the highest value:
    return max(lang_count.keys(), key=(lambda k: lang_count[k]))