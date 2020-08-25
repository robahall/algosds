class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head):
    """
    Using recursion
    """
    if not head or not head.next:
        return head
    first_node = head
    second_node = head.next

    first_node.next = swapPairs(second_node.next)
    second_node.next = first_node
    return second_node

def swapPairsIter(head):
    # Dummy node acts as the prevNode for the head node
    # of the list and hence stores pointer to the head node.
    dummy = ListNode(-1)
    dummy.next = head

    prev_node = dummy

    while head and head.next:
        #Nodes to be swapped
        first_node = head
        second_node = head.next

        #Swapping
        prev_node.next = second_node
        first_node.next = second_node.next
        second_node.next = first_node

        #Reinitializing the head and prev node for next swap
        prev_node = first_node
        head = first_node.next

    return dummy.next

def swapPairsSimpleIter(head):
    curr = head
    while curr and curr.next:
        curr.val, curr.next.val = curr.next.val, curr.val
        curr = curr.next.next
    return head


if __name__ == "__main__":
    linked_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    #new = swapPairs(linked_list)
    #new_iter = swapPairsIter(linked_list)
    swapPairsSimpleIter(linked_list)