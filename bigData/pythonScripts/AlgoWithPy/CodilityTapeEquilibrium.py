__author__ = 'ahmed'


def solution(ArrayList):
    itemRightArray = []
    itemLeftArray = []
    resultArray = []

    for ranger in range(len(ArrayList)-1):
        itemRightArray.append(sum(ArrayList[ranger+1:]))
        itemLeftArray.append(sum(ArrayList[:ranger+1]))

    for itemInRange in range(len(itemRightArray)):
        resultArray.append(abs(itemLeftArray[itemInRange] - itemRightArray[itemInRange]))

    return resultArray


def solution100(Array):
    arrayToProcess = Array
    arrayForFirstProcessing = []
    arrayResult = []
    sumArray = 0
    if len(arrayToProcess) == 2:
        return abs(arrayToProcess[0] - arrayToProcess[1])
    for rangerInArray in arrayToProcess:
        sumArray = sumArray + rangerInArray
        arrayForFirstProcessing.append(sumArray)
        print arrayForFirstProcessing

    for resultRanger in range(len(arrayForFirstProcessing)-1):
        resultArrayPreProcessing = (sumArray - 2 * arrayForFirstProcessing[resultRanger])
        print sumArray, arrayForFirstProcessing[resultRanger], resultArrayPreProcessing
        arrayResult.append(abs(resultArrayPreProcessing))

    arrayResult.sort()
    return arrayResult[0]

solution100([3,1,2,4,3])