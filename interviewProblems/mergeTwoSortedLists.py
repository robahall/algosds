class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2):
    """
    Recurrence relation: {list1[0] + merge(list1[1:], list2) list1[0] <list[0]
                          {list2[0] + merge(list1, list2[1:]) otherwise
    Base Case: f(next) = None
    :param head:
    :return:
    """
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    elif l1.val < l2.val:
        l1.next = mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoLists(l1, l2.next)
        return l2

def mergeTwoListsIter(l1, l2):
    prehead = ListNode(-1)

    prev = prehead
    while l1 and l2:
        if l1.val <= l2.val:
            prev.next = l1
            l1 = l1.next
        else:
            prev.next = l2
            l2 = l2.next
        prev = prev.next

    prev.next = l1 or l2

    return prehead.next




if __name__ == "__main__":
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    l3 = mergeTwoLists(l1, l2)
    print(l3)