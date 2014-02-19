__author__ = 'ahmed'

import Stack

stringWithPara = "{[()()()()()(){}{}{}[](((([()))))()()()((((()))))((((()))))()()()()][]}"

def checkForBalance(stringToCheck):
    paraStack = Stack.Stack()
    for item in stringToCheck:
        if item in "({[":
            paraStack.push(item)
        else:
            if paraStack.isEmpty():
                return False
            else:
                top = paraStack.pop()
                if not matches(top, item):
                    return False

    if paraStack.isEmpty():
        return True
    else:
        return False

def matches(open, close):
    opens = "({["
    closes = ")}]"
    return  opens.index(open) == closes.index(close)

print checkForBalance(stringWithPara)

