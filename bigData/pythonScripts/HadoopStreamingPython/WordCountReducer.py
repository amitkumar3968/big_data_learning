#!/usr/bin/env python

import sys
import re

current_word = None
current_count = 0
word = 0


for line in sys.stdin:
    line = re.sub('[^A-Za-z0-9\\t]','',line)
    word, count = line.split("\t")

    try:
        count = int(count)
    except ValueError:
        continue

    if current_word == word:
        current_count = current_count + count
    else:
        if current_word:
            print(current_word, current_count)
        current_word = word
        current_count = count

if current_word == word:
    print(current_word, current_count)


