class TreeNode:
    """
    Definition of a binary tree node.
    """
    def __init__(self, x, left = None, right= None):
        self.val = x
        self.left = left
        self.right = right


def maxDepth(root):
    if not root:
        return 0
    elif root.left is None and root.right is None:
        return 1
    else:
        return max(maxDepth(root.left), maxDepth(root.right)) + 1

if __name__ == "__main__":
    tree = TreeNode(3, TreeNode(9, None, None),
                             TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None)))

    print(maxDepth(tree))