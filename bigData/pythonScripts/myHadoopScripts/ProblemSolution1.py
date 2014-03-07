__author__ = 'ahmed'


'''
  A[0] =  1
  A[1] =  4
  A[2] = -1
  A[3] =  3
  A[4] =  2

'''
anotherList = []
myList = [1,4,5,3,2,6,-1]
def processingFunc(info):
    if myList[info] == -1:
        anotherList.append(-1)
        return int(len(anotherList))
    else:
        x = myList[info]
        anotherList.append(x)
        return processingFunc(x)

print processingFunc(0)
