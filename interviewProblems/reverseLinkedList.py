class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseListRecursive(head):
    """
    Recurrence relation: f(next) = head.next
    Base Case: f(next) = None
    :param head:
    :return:
    """
    if not head or not head.next:
        return head

    node = reverseListRecursive(head.next)
    head.next.next = head
    head.next = None
    return node






if __name__ == "__main__":
    linked_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    reverseListRecursive(linked_list)