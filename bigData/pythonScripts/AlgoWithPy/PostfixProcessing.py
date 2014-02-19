__author__ = 'ahmed'

from Stack import Stack

stringToProcess = "912 121 123 + 126 12 * 127 + * *"
#stringToProcess = "13++123+232"
ERROR = -99999

def PostFixSingleCharProcessing(stringToProcess):
    processingList = [char for char in stringToProcess]
    postFixStack = Stack()
    for items in processingList:
        if items.isdigit():
            postFixStack.push(float(items))
        else:
            if not postFixStack.isEmpty():
                operandSecond = postFixStack.pop()
            else:
                return ERROR
            if not postFixStack.isEmpty():
                operandFirst = postFixStack.pop()
            else:
                return ERROR
            result = operationProcessing(items, operandFirst, operandSecond)
            if result != -99999:
                postFixStack.push(result)
            else:
                return ERROR
    return postFixStack.pop()

def PostFixProcessing(stringToProcess):
    processingList = stringToProcess.split()
    postFixStack = Stack()
    for items in processingList:
        if items.isdigit():
            postFixStack.push(float(items))
        else:
            if not postFixStack.isEmpty():
                operandSecond = postFixStack.pop()
            else:
                return ERROR
            if not postFixStack.isEmpty():
                operandFirst = postFixStack.pop()
            else:
                return ERROR
            result = operationProcessing(items, operandFirst, operandSecond)
            if result != -99999:
                postFixStack.push(result)
            else:
                return ERROR
    return postFixStack.pop()

def operationProcessing(operator, operandFirst, operandSecond):
    if operator == "*":
        return operandFirst * operandSecond
    elif operator == "/":
        return operandFirst / operandSecond
    elif operator == "+":
        return operandFirst + operandSecond
    elif operator == "-":
        return operandFirst - operandSecond
    else:
        return ERROR

#result = PostFixSingleCharProcessing(stringToProcess)
result = PostFixProcessing(stringToProcess)
if result == ERROR:
    print("ERROR")
else:
    print result