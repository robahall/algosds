
class Node:
    def __init__(self, value, nextNode = None):
        self.value = value
        self.next = nextNode


class MyCircularQueue:

    def __init__(self, k: int):
        """
        :param k: (int) sets size of queue
        """
        self.capacity = k
        self.head = None
        self.tail = None
        self.count = 0

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue.
        :param value: (int) Value to insert
        :return: (bool) True if successful
        """
        if self.count == self.capacity:
            return False

        if self.count == 0:
            self.head = Node(value)
            self.tail = self.head
        else:
            newNode = Node(value)
            self.tail.next = newNode
            self.tail = newNode
        self.count += 1
        return True

    def deQueue(self) -> bool:
        """
        Deletes an element from the circular queue. Return true if successful.
        """
        if self.count == 0:
            return False
        self.head = self.head.next
        self.count -= 1
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue
        :return: (int) item
        """
        if self.count == 0:
            return -1
        return self.head.value

    def Rear(self) -> int:
        if self.count == 0:  # empty queue
            return -1
        return self.tail.value

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty.
        :return: (bool) returns True if empty
        """
        return self.count == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        :return: (bool) returns True if full
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
