## Frm leetcode linked list



class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 0
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -addAtIndexaddAtIndex1.
        """
        if self.head == None:
            self.addAtHead(index)
        x = self.head
        if index < self.size:
            for _ in range(index):
                x = x.next
            return x.key
        return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if not self.head:
            self.head = Node(val)
        else:
            new_node = Node(val)
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if not self.head:
            self.head = Node(val)
        else:
            x = self.head
            for _ in range(self.size - 1):
                x = x.next
            x.next = Node(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index == self.size:
            self.addAtTail(val)
        else:
            if index < self.size:
                x = self.head
                for _ in range(index - 1):
                    x = x.next
                new_node = Node(val)
                new_node.next = x.next
                x.next = new_node
                self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < self.size:
            x = self.head
            if index == 0:
                self.head = x.next
            else:
                for _ in range(index - 1):
                    x = x.next
                x.next = x.next.next
                self.size -= 1

if __name__ == "__main__":
    obj = MyLinkedList()
    obj.addAtHead(1)
    obj.addAtTail(3)
    obj.addAtIndex(1,2)
    obj.get(1)
    obj.deleteAtIndex(1)
    obj.get(1)