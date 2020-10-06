class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def isPalindrome(head):
    """
    Complexity = O(n) -> One pass through
    Space = O(n) -> created new array
    """
    if not head.next:
        return False
    vals = []
    x = head
    while x:
        vals.append(x.val)
        x = x.next
    return vals[:] == vals[::-1]

def isPalindromeRecursive(head):
    front_pointer = head
    def recursive_check(current_node = head):
        if current_node is not None:
            if not recursive_check(current_node.next):
                return False
            if front_pointer.val != current_node.val:
                return False
            front_pointer = front_pointer.next
        return True
    return recursive_check()



if __name__ == "__main__":
    ll = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=2, next=ListNode(val=1))))
    print(isPalindrome(ll))
    ll2 = ListNode(val=1)
    print(isPalindrome(ll2))
    ll3 = ListNode(val=1, next=ListNode(val=0, next=ListNode(val=0)))
    print(isPalindrome(ll3))
    

