__author__ = 'ahmed'

import random
def solution(A):
    if len(A) != 0:
        maxOfArray = max(A)
        totalArray = maxOfArray * (maxOfArray - 1) / 2

        maxLen = len(A)
        totalIndex = maxLen * (maxLen - 1) / 2

        if totalArray == totalIndex:
            return 1
        else:
            return 0
    else:
        return 0

print solution([1,2,3,5,4,6])
count = 0
for item in random.sample(xrange(1,100000),100000-1):
    count = count + 1

print count