# Time complexity: O(1)
# Space Complexity: O(N)
# Thread safe utilizing locking

from threading import Lock

class MyCircularQueue:

    def __init__(self, k: int):
        """
        tailIndex = (headIndex + count - 1 ) % capacity
        :param k: size of queue
        """
        self.capacity = k  # Array size/or length
        self.queue = [0] * k  # the queue
        self.count = 0  # current length of queue
        self.headIdx = 0  # current head index
        self.queueLock = Lock()  # Additional attribute to protect the access of our queue.

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue.
        :param value: (int) Value to insert
        :return: (bool) True if successful
        """
        with self.queueLock:
            if self.count == self.capacity:
                return False
            self.queue[(self.headIdx + self.count) % self.capacity] = value
            self.count += 1
        #automatically releases the lock when leaving the block
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue.
        :return: (bool) True if successful
        """
        if self.count == 0:
            return False
        self.headIdx = (self.headIdx + 1) % self.capacity
        self.count -= 1
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.count == 0:
            return -1
        return self.queue[self.headIdx]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.count == 0:
            return -1
        return self.queue[(self.headIdx + self.count -1) % self.capacity]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.count == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.count == self.capacity


if __name__ == "__main__":
    obj = MyCircularQueue(3)
    obj.enQueue(5)
    obj.enQueue(4)
    obj.enQueue(3)
    obj.enQueue(2)
    obj.Rear()
    obj.isFull()
    obj.deQueue()
    obj.enQueue(4)
    obj.Rear()
