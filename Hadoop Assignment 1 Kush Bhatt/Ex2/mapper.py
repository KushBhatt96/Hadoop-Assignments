#!/usr/bin/env python
"""mapper.py"""
import sys
import string

for line in sys.stdin:
    line = line.strip()

    if line == "":
        continue

    line = line.lower()

    strippable = string.punctuation + string.digits

    for c in strippable:
        if c in line:
            line = line.replace(c, " ")

    words = line.split()

    index = 0
    while(index < len(words)-1):
        bigram = [words[index], words[index+1]]
        print('%s\t%s' % (bigram, 1))
        index += 1