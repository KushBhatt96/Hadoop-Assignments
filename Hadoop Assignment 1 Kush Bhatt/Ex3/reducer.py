#! /usr/bin/python

from sys import stdin
import re

index = {}

for line in stdin:
        word, fnames = line.split('\t', 1)

        index.setdefault(word, [])

        for fname in fnames.split(','):
            fname = fname.strip()
            if(fname not in index[word]):
                index[word].append(fname)

for word in index:
        print('%s\t%s' % (word, index[word]))