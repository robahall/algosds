class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def addAtTail(self, val):
        if not self.head:
            self.head = ListNode(val)

        else:
            x = self.head
            for _ in range(self.size -1):
                x = x.next
            x.next = ListNode(val)
        self.size +=1


    def deleteNode(self, node):
        x = self.head
        while x.next:
            if x.next.val == node:
                val = x.next.next
                del(x.next)
                x.next = val
            x = x.next


if __name__ == "__main__":
    ll = MyLinkedList()
    ll.addAtTail(4)
    ll.addAtTail(1)
    ll.addAtTail(9)
    ll.addAtTail(5)
    ll.addAtTail(10)
    ll.deleteNode(5)
