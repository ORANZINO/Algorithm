class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.front = 0
        self.rear = -1
        self.arr = [-1] * k
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.size == self.k:
            return False
        self.size += 1
        if self.rear == self.k - 1:
            self.rear = 0
        else:
            self.rear += 1
        self.arr[self.rear] = value
        return True

    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        self.size -= 1
        self.arr[self.front] = -1
        if self.size == 0:
            self.front, self.rear = 0, -1
        elif self.front == self.k - 1:
            self.front = 0
        else:
            self.front += 1
        return True

    def Front(self) -> int:
        return self.arr[self.front] if self.size != 0 else -1

    def Rear(self) -> int:
        return self.arr[self.rear] if self.size != 0 else -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k