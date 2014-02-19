__author__ = 'ahmed'

from Stack import Stack

NumberToProcess = 1000

def devBy2(Number):
    storageStack = Stack()
    binaryData = ""
    while Number > 0:
        storageStack.push(Number%2)
        Number = Number // 2

    while not storageStack.isEmpty():
        binaryData = binaryData + str(storageStack.pop())

    return binaryData

def devByX(Number, base):
    digits="0123456789ABCDEF"
    storageStack = Stack()
    binaryData = ""
    while Number > 0:
        storageStack.push(Number%base)
        Number = Number // base

    while not storageStack.isEmpty():
        binaryData = binaryData + digits[storageStack.pop()]

    return binaryData


print devBy2(NumberToProcess)
print(devByX(26,26))