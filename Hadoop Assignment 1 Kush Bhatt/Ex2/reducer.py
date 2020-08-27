#!/usr/bin/env python
"""reducer.py"""

import sys

current_bigram = None
current_count = 0
bigram = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # split the output from the mapper into separate variables
    bigram, count = line.split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        continue

    if current_bigram is None:
        current_bigram = bigram
        current_count += count
    elif current_bigram == bigram:
        current_count += count
    else:
        # write result to STDOUT
        print('%s\t%s' % (current_bigram, current_count))
        current_count = count
        current_bigram = bigram

print('%s\t%s' % (current_bigram, current_count))