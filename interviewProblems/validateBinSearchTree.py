
class TreeNode:
    """
    Definition of a binary tree node.
    """
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

def isValidBST(root):
    if not root:
        return False

    def helper(node, lower=float('-inf'), upper=float('inf')):
        if not node:
            return True
        val = node.val
        if val <= lower or val >= upper:
            return False
        if not helper(node.right, val, upper):
            return False
        if not helper(node.left, lower, val):
            return False
        return True
    return helper(root)


if __name__ == "__main__":
    tree_1 = TreeNode(3, TreeNode(1), TreeNode(3))
    tree_2 = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    print(isValidBST(tree_2))

