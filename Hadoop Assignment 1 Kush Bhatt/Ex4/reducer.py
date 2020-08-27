#! /usr/bin/python

import sys

current_word = None
current_letter = None

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    
    letter, word = line.split('.', 1)

    if current_letter == None:
        current_letter = letter
        current_word = word
    elif current_word == word:
        continue
    else:
        print(current_word)
        current_word = word
        current_letter = letter
print(current_word)