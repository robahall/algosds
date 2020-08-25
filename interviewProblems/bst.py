class TreeNode:
    """
    Definition of a binary tree node.
    """
    def __init__(self, x, left = None, right= None):
        self.val = x
        self.left = left
        self.right = right


def searchBST(root, val):
    """
    Search a b-tree for a subtree with subroot of val
    Recursion Relation:
    root = root(left, right) -> val =
    :param root:
    :param val:
    :return:
    """
    if root is None or val == root.val:
        return root

    return searchBST(root.left, val) if val < root.val else searchBST(root.right, val)

if __name__ == "__main__":
    root = TreeNode(4, TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None)), TreeNode(7, None, None))
    out = searchBST(root, 2)
