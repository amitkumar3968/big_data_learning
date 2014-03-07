__author__ = 'ahmed'

import re
stackData = []


'''
Stack Operations Class
'''
class StackOperations:
    def __init__(self):
        pass

    def pushToStack(self, data):
        stackData.append(data)

    def popTwoFromStack(self):
        stackPoped = []
        if len(stackData) >= 2:
            stackPoped.append(stackData[len(stackData) - 1])
            stackPoped.append(stackData[len(stackData) - 2])
            stackData.pop(len(stackData)-1)
            stackData.pop(len(stackData)-1)
        elif len(stackData) < 2:
            return [-1]
        return stackPoped

'''
Math Operations Class
'''

class MathOperations:

    def adderFunction(self, firstValue, secondValue):
        return firstValue + secondValue


    def multiplierFunction(self, firstValue, secondValue):
        return firstValue * secondValue

'''
Data Processing Operations
'''
class DataProcessingOps():

    def dataProcessing(self, data):
        dataToProcess = []
        if data == "*":
            dataToProcess = StackOperations().popTwoFromStack()
            if dataToProcess[0] != -1:
                StackOperations().pushToStack(MathOperations().multiplierFunction(int(dataToProcess[0]), int(dataToProcess[1])))
            else:
                print "String Incorrect"
                exit()
        elif data == "+":
            dataToProcess = StackOperations().popTwoFromStack()
            if dataToProcess[0] != -1:
                StackOperations().pushToStack(MathOperations().adderFunction(int(dataToProcess[0]), int(dataToProcess[1])))
            else:
                print "String InCorrect"
                exit()
        else:
            StackOperations().pushToStack(data)

    def preProcessing(self, stringPreProcess):
        if stringPreProcess.find("++") != -1 or stringPreProcess.find("++") != -1:
            return -1
        if len(re.findall('\d\d\d+',stringPreProcess)) != 0:
            return -1
        else:
            print "Continue Processing"
            return SolutionsOps().solution(stringPreProcess)

'''
Solutions Class
'''
class SolutionsOps:
    def solution(self, stringProc):
        for items in stringProc:
            DataProcessingOps().dataProcessing(items)
        return int(stackData[0])

'''
Checking for Main for Testing.
'''
def solution(A):
    stringForProcessing = []
    stringForProcessing.append(A)
    for item in stringForProcessing:
        stackData = []
        afterProcessing = DataProcessingOps().preProcessing(item)
        print "String we are Processing Now is %s", item
        print "Result After processing is %s" %afterProcessing

solution('913+62*7+**')
solution('13++123+232')