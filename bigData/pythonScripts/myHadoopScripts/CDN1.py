anotherList = []
myList = []
def processingFunc(info):
    if myList[info] == -1:
        anotherList.append(-1)
        return int(len(anotherList))
    else:
        x = myList[info]
        anotherList.append(x)
        return processingFunc(x)


def solution(A):
    myList = A
    return processingFunc(0)

print solution([1,4,5,3,2,6,-1])