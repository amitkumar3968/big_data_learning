__author__ = 'ahmed'

def solution(X, Y, D):
    result = (float(Y) - float(X)) / float(D)
    if result%1 == 0:
        return int(result)
    else:
        return int(result)+1

print solution(12, 85, 12)

