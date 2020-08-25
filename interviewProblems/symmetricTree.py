class TreeNode:
    """
    Definition of a binary tree node.
    """
    def __init__(self, x, left = None, right= None):
        self.val = x
        self.left = left
        self.right = right


def isSymemetricIterative(root):
    if root is None:
        return True
    q = []
    q.append(root)
    q.append(root)

    while q:
        t1 = q.pop()
        t2 = q.pop()
        if not t1 and not t2:
            continue
        if not t1 or not t2:
            return False
        if t1.val != t2.val:
            return False
        q.append(t1.left)
        q.append(t2.right)
        q.append(t1.right)
        q.append(t2.left)

    return True

def isSymmetricRecursive(root):
    def isMirror(t1, t2):
        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None:
            return False
        return (t1.val == t2.val) and isMirror(t1.right, t2.left) and isMirror(t1.left, t2.right)

    return isMirror(root, root)
