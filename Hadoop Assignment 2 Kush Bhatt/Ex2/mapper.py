#!/usr/bin/env python
"""mapper.py"""

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split up the line
    node, rest = line.split('\t', 1)
    adj_list, dist, color, parent = rest.split('|')

    if color == "WHITE" or color == "BLACK":
        print(node + "\t" + adj_list + "|" + dist + "|" + color + "|" + parent)
    elif color == "GRAY":
        print(node + "\t" + adj_list + "|" + dist + "|" + "BLACK" + "|" + parent)
        for child in adj_list.split(","):
            print(child + "\t" + "null" + "|" + str(int(dist)+1) + "|" + "GRAY" + "|" + node)