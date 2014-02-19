__author__ = 'ahmed'

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        return self.items.insert(0, item)

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop()

    def size(self):
        return len(self.items)

    def printQ(self):
        print self.items

if __name__=="__main__":
    q = Queue()
    print q.isEmpty()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print q.size()
    q.printQ()
    print q.dequeue()
    print q.dequeue()
    print q.dequeue()
    print q.dequeue()
    print q.dequeue()

