#!/usr/bin/env python

from sys import stdin
import re
import os
import string

for line in stdin:
        # Get the file path
        path = os.environ["map_input_file"]
        path = re.findall(r'\w+', path)

        # Get the name of the file from the path
        fname = path[-2] + "." + path[-1]

        line = line.strip()

        if line == "":
                continue

        line = line.lower()

        strippable = string.punctuation + string.digits

        for c in strippable:
                if c in line:
                        line = line.replace(c, " ")

        # Get an array of all the words inside the document
        words = line.split()

        # Map the words
        for word in words:
                print("%s\t%s" % (word, fname))