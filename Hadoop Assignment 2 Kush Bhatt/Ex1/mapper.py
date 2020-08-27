#!/usr/bin/env python
"""mapper.py"""

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into row, column, and value
    cell_info = line.split(',')
    
    print ('%s\t%s' % (cell_info[1]+","+cell_info[0], cell_info[2]))