class TreeNode:
    """
    Definition of a binary tree node.
    """
    def __init__(self, x, left = None, right= None):
        self.val = x
        self.left = left
        self.right = right

def preorderTraversal(root: TreeNode):
    """
    Preorder traversal of tree using recursion where we push nodes into the output list in the following order:
    Top -> Bottom and Left -> Right
    Time complexity: O(N) -> visit each node (N) once
    Space complexity: O(N) -> depending on structure we can keep the entire tree.
    :param root: (TreeNode Obj) Top of tree.
    :return: Order of analysis
    """
    output = []
    if not root:
        return (output)

    def helper(node):
        if not node:
            return
        output.append(node.val)
        helper(node.left)
        helper(node.right)
    helper(root)
    return output

def inorderTraversal(root: TreeNode):
    """
    inorder traversal of tree using recursion where we push nodes into the output list in the following order:
    Top -> Bottom and Left -> Right
    Time complexity: O(N) -> visit each node (N) once
    Space complexity: O(N) -> depending on structure we can keep the entire tree.
    :param root: (TreeNode Obj) Top of tree.
    :return: Order of analysis
    """
    output = []
    if not root:
        return (output)

    def helper(node):
        if not node:
            return
        helper(node.left)
        output.append(node.val)
        helper(node.right)
    helper(root)
    return output

def postorderTraversal(root: TreeNode):
    """
    Postorder traversal of tree using recursion where we push nodes into the output list in the following order:
    Top -> Bottom and Left -> Right
    Time complexity: O(N) -> visit each node (N) once
    Space complexity: O(N) -> depending on structure we can keep the entire tree.
    :param root: (TreeNode Obj) Top of tree.
    :return: Order of analysis
    """
    output = []
    if not root:
        return (output)

    def helper(node):
        if not node:
            return
        helper(node.left)
        helper(node.right)
        output.append(node.val)
    helper(root)
    return output


if __name__ == "__main__":
    #bin_tree_order = [1, None, 2, 3]
    root = TreeNode(1, None, TreeNode(2, TreeNode(3, None, None), None))
    print(preorderTraversal(root))
    print(inorderTraversal(root))
    print(postorderTraversal(root))