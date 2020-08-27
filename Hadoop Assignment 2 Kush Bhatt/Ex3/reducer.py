#!/usr/bin/env python
"""reducer.py"""
import sys

current_pair = None
current_count = 0
current_total = 0
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the input we got from mapper.py
    pair, count = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_pair is None:
        current_pair = pair
    if current_pair == pair:
        current_count += count
    else:
        if "*" not in current_pair:
            print('%s\t%s' % (current_pair, (float(current_count)/float(current_total))))
        if "*" in current_pair:
            current_total = current_count
        current_pair = pair
        current_count = count

print('%s\t%s' % (current_pair, (float(current_count)/float(current_total))))
