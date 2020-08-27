#! /usr/bin/python
import sys
import string

for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()
    if line == "":
        continue

    line = line.lower()

    strippable = string.punctuation + string.digits

    for c in strippable:
        if c in line:
            line = line.replace(c, " ")

    # word is the key
    for word in line.split():
        if word != "":
            print((word[0]+'.'+word))
