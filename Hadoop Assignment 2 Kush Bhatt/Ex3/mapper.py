#!/usr/bin/env python
"""mapper.py"""

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    values = line.split()
    x = 0
    y = 0
    while(x < len(values)):
        y = 0
        while(y < len(values)):
            if(x!=y):
                print(values[x] + "," + values[y] + "\t" + "1")
                print(values[x] + "," + "*" + "\t" + "1")
            y += 1
        x += 1
