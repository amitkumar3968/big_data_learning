__author__ = 'ahmed'

def solution(A):
    if len(A) != 0:
        totalValue = sum(A)
        totalIndex = sum(range(1, len(A)+1))
        if totalIndex == totalValue:
            return max(A) + 1
        else:
            result = max(A) - (abs(totalIndex - totalValue))
            return result
    else:
        return 1


print solution([1,4,3,5,6,7,8,9,10])