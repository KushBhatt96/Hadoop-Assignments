#!/usr/bin/env python
"""reducer.py"""

import sys

current_cell = None
current_value = None
cell = None
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    cell, value = line.split('\t', 1)    # 1 represents the maxsplit value

    if current_cell:
        print('%s,%s' % (current_cell, current_value))
    current_cell = cell
    current_value = value

# do not forget to output the last word if needed!
if current_cell == cell:
    print ('%s,%s' % (current_cell, current_value))