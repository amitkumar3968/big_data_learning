#!/usr/bin/env python
import sys
import re

for line in sys.stdin:
    line = re.sub('[^A-Za-z\ ]+','',line)
    #line = re.sub('[^A-Za-z0-9\ ]+','',line)
    line = line.strip().lower()
    words = line.split()
    for word in words:
        print("%s\t%s"%(word,1))

