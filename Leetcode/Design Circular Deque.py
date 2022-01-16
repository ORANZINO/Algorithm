class MyCircularDeque:

    def __init__(self, k: int):
        self.q = [None] * k
        self.maxlen = k
        self.front, self.rear = k - 1, 0
        self.size = 0

    def convert(self, x):
        if x == self.maxlen:
            return 0
        elif x == -1:
            return self.maxlen - 1
        else:
            return x

    def insertFront(self, value: int) -> bool:
        if self.size == self.maxlen:
            return False
        self.size += 1
        self.q[self.front] = value
        self.front = self.convert(self.front - 1)
        return True

    def insertLast(self, value: int) -> bool:
        if self.size == self.maxlen:
            return False
        self.size += 1
        self.q[self.rear] = value
        self.rear = self.convert(self.rear + 1)
        return True

    def deleteFront(self) -> bool:
        if self.size == 0:
            return False
        self.size -= 1
        self.front = self.convert(self.front + 1)
        self.q[self.front] = None
        return True

    def deleteLast(self) -> bool:
        if self.size == 0:
            return False
        self.size -= 1
        self.rear = self.convert(self.rear - 1)
        self.q[self.rear] = None
        return True

    def getFront(self) -> int:
        temp = self.q[self.convert(self.front + 1)]
        return -1 if temp is None else temp

    def getRear(self) -> int:
        temp = self.q[self.convert(self.rear - 1)]
        return -1 if temp is None else temp

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.maxlen

    