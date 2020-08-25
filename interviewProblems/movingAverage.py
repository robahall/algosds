class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        tail = (self.headIdx + count -1 ) % capacity
        """

        self.capacity = size
        self.queue = [0] * size
        self.count = 0
        self.headIdx = 0

    def enQueue(self, value):
        if self.isFull():
            return False
        self.queue[(self.headIdx + self.count) % self.capacity] = value
        self.count += 1
        return True

    def deQueue(self):
        if self.isEmpty():
            return False
        self.headIdx = (self.headIdx + 1) % self.capacity
        self.count -= 1
        return True

    def Front(self):
        if self.isEmpty():
            return -1
        return self.queue[self.headIdx]

    def Rear(self):
        if self.isEmpty():
            return -1
        return self.queue[(self.headIdx + self.count - 1) % self.capacity]

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.capacity

    def movingAverage(self):
        return sum(self.queue) / self.count

    def next(self, val: int) -> float:
        if self.isFull():
            self.deQueue()
        self.enQueue(val)
        return self.movingAverage()

if __name__ == "__main__":
    ma = MovingAverage(3)
    print(ma.next(1))  # 1
    print(ma.next(2))  # 1.5
    print(ma.next(3))  # 2
    print(ma.next(4))  # 3
    print(ma.next(5))  # 4
    print(ma.next(6))  # 5
