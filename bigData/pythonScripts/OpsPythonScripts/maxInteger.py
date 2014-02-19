import heapq as heapQueue
def heapsort(iterable):
    'Equivalent to sorted(iterable)'
    h = []
    for value in iterable:
        heapQueue.heappush(h, value)
    return [heapQueue.heappop(h)]

print heapsort([9,6,3,8,6,0,1,5,7,9])


