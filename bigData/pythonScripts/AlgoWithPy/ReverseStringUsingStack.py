__author__ = 'ahmed'

import test

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def pop(self):
        return self.items.pop()

    def push(self, item):
        return self.items.append(item)

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def printStach(self):
        print self.items

if __name__ == "__main__":
    stringToReverse = "My Name is Zubair AHMED and I am working in Saggezza"
    stringReverseStack = Stack()
    for item in stringToReverse:
        stringReverseStack.push(item)

    reverseString = ""
    while not stringReverseStack.isEmpty():
        reverseString = reverseString + stringReverseStack.pop()

    print reverseString