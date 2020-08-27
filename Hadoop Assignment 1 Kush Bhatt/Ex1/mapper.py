#!/usr/bin/env python
"""mapper.py"""
import sys
import random

for line in sys.stdin:

    # remove leading and trailing whitespace
    line = line.strip()

    # The following code will skip any blank lines
    if line == "":
        continue

    # If the random number generated from 1-10 is 5 then output the line
    if random.randint(1, 10) == 5:
        print('%s\t%s' % (line, 1))
