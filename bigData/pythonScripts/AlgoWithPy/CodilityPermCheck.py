__author__ = 'ahmed'

def solution(A):
    if len(A) != 0:
        totalArray = sum(A)
        totalIndex = sum(range(1,len(A)+1))

        if totalArray == totalIndex:
            return 1
        else:
            return 0
    else:
        return 0

