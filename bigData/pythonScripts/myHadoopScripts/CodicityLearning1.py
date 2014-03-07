__author__ = 'ahmed'

def solution(Array):
    # write your code in Python 2.6
    print Array
    minDifference = []
    for item in range(0,len(Array)):
        firstSplit = 0
        secondSplit = 0
        for firstSplitIterator in range(0,item+1):
            firstSplit = firstSplit + Array[firstSplitIterator]
        for secondSplitIterator in range(item+1,len(Array)):
            secondSplit = secondSplit + Array[secondSplitIterator]
        if firstSplit !=0 and secondSplit !=0:
            minDifference.append(abs(firstSplit - secondSplit))
    return min(minDifference)

def solution_2(Array):
    # write your code in Python 2.6
    minDifference = []
    for item in range(0,len(Array)):
        firstSplit = []
        secondSplit = []
        firstSplit.append(Array[:item+1])
        secondSplit.append(Array[item+1:])
        minDifference.append(abs(sum(firstSplit[0]) - sum(secondSplit[0])))
    print "------------------"
    print minDifference
    return min(minDifference)

print solution_2([1,2,3,4,5,6,7,8])