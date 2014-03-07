def solution(A):
    # write your code in Python 2.6
    dictionary = dict()
    for iterator in range(len(A)):
        if A[iterator] not in dictionary:
            dictionary[A[iterator]] = [iterator]
        else:
            dictionary[A[iterator]].append(iterator)
    count = 0
    for items in dictionary:
        if len(dictionary[items]) <= 1:
            continue
        else:
            count = count + len(dictionary[items])
    return count - 1