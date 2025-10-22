#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)

import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True

def get_sentence():
    user_sentence = input("Enter a sentence: ")

    while (is_sentence(user_sentence) == False):
        print("This does not meet the criteria for a sentence.")
        user_sentence = input("Enter a sentence: ")

    return user_sentence

def calculate_frequencies():
    global words
    global frequencies

    isCopy = 0
    currentWord = ""
    splitSentence = re.split(r'[, \s]+', user_sentence)
    
    for i in range(0, len(splitSentence)):
        currentWord = splitSentence[i].lower()
        isCopy = 0
        for e in range(0, len(words)):
            if words[e] == currentWord:
                isCopy = 1
                frequencies[e] += 1
        if isCopy == 0:
            words.append(currentWord)
            frequencies.append(1)

def print_frequencies(words, frequencies):
    for i in range(0, len(words)):
        print("{}: {}".format(words[i], frequencies[i]))

sentence = get_sentence()

words = []
frequencies = []

calculate_frequencies()

print_frequencies(words, frequencies)
