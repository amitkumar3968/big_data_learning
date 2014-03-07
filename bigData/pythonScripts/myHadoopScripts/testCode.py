import re
stackData = []


def pushToStack(data):
    stackData.append(data)

def popTwoFromStack():
    stackPoped = []
    if len(stackData) >= 2:
        stackPoped.append(stackData[len(stackData) - 1])
        stackPoped.append(stackData[len(stackData) - 2])
        stackData.pop(len(stackData)-1)
        stackData.pop(len(stackData)-1)
    elif len(stackData) < 2:
        return [-1]
    return stackPoped


def adderFunction(firstValue, secondValue):
    return firstValue + secondValue


def multiplierFunction(firstValue, secondValue):
    return firstValue * secondValue


def dataProcessing(data):
    dataToProcess = []
    if data == "*":
        dataToProcess = popTwoFromStack()
        if dataToProcess[0] != -1:
            pushToStack(multiplierFunction(int(dataToProcess[0]), int(dataToProcess[1])))
        else:
            print "String Incorrect"
            exit()
    elif data == "+":
        dataToProcess = popTwoFromStack()
        if dataToProcess[0] != -1:
            pushToStack(adderFunction(int(dataToProcess[0]), int(dataToProcess[1])))
        else:
            print "String InCorrect"
            exit()
    else:
        pushToStack(data)

def solution(stringProc):
    for items in stringProc:
        dataProcessing(items)
    return int(stackData[0])


def preProcessing(stringPreProcess):
    if stringPreProcess.find("++") != -1 or stringPreProcess.find("++") != -1:
        return -1
    if len(re.findall('\d\d\d+',stringPreProcess)) != 0:
        return -1
    else:
        print "Continue Processing"
        return solution(stringPreProcess)

if __name__ == '__main__':
    stringProcessing = ["13+62*7+*","43+69*9+*","13++123+232", "43+78++", "123+453+*"]
    for item in stringProcessing:
        stackData = []
        afterProcessing = preProcessing(item)
        print "String we are Processing Now is %s", item
        print "Result After processing is %s" %afterProcessing
