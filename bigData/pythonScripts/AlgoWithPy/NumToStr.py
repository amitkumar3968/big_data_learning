__author__ = 'ahmed'


def toStr(num, base):
    indexer = "0123456789ABCDEF"
    if num < base:
        return indexer[num]
    else:
        return toStr(num//base,base) + indexer[num%base]

def reverseStringRecu(stringData, index):
    if index == len(stringData):
        return stringData[index]
    else:
        return reverseStringRecu(stringData[index+1], index+1) + stringData[index]


print reverseStringRecu("Hello", 0)