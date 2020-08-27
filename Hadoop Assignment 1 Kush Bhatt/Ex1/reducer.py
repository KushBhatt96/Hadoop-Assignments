#!/usr/bin/env python
"""reducer.py"""
import sys

for line in sys.stdin:

    # remove leading and trailing whitespace
    line = line.strip()

    # split the key and value from mapper and take only the key (line)
    line = line.split('\t')[0]

    # output the lines
    print('%s\t%s' % (line, ''))