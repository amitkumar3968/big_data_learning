__author__ = 'ahmed'
'''

  A[0] = 3
  A[1] = 5
  A[2] = 6
  A[3] = 3
  A[4] = 3
  A[5] = 5
   0 <= P < Q < N and A[P] = A[Q]
'''


myList = [3,5,6,3,3,5]
dictionary = dict()
for item in range(len(myList)):
    dictionary[item] = myList[item]
