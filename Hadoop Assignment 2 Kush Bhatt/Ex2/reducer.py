#!/usr/bin/env python
"""reducer.py"""
import sys

current_node = "null"
current_adj_list = "null"
current_dist = sys.maxsize
current_parent = "null"
current_color = "WHITE"

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    node, rest = line.split('\t', 1)
    adj_list, dist, color, parent = rest.split('|')

    if dist == "Integer.MAX_VALUE":
        dist = sys.maxsize
    else:
        dist = int(dist)

    if current_node == "null":
        current_node = node
    if current_node == node:
        if adj_list != "null":
            current_adj_list = adj_list
        if dist != "null" and dist < current_dist:
            current_dist = dist
            current_parent = parent
        if color == 'BLACK' and (current_color != "BLACK"):
            current_color = color
        elif color == 'GRAY' and current_color == "WHITE":
            current_color = color
    else:
        print(current_node + "\t" + current_adj_list + "|" + str(current_dist) + "|" + current_color + "|" + current_parent)
        current_node = node
        current_adj_list = adj_list
        current_dist = dist
        current_color = color
        current_parent = parent

print(current_node + "\t" + current_adj_list + "|" + str(current_dist) + "|" + current_color + "|" + current_parent)
