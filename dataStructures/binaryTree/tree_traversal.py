from collections import deque

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
    Preorder traversal of tree using interations where we push nodes into the output list in the following order:
    Top -> Bottom and Left -> Right
    Time complexity: O(N) -> visit each node (N) once
    Space complexity: O(N) -> depending on structure we can keep the entire tree.
    :param root: (TreeNode Obj) Top of tree.
    :return: Order of analysis
    """
    if root is None:
        return []

    stack, output = [root, ], []

    while stack:
        root = stack.pop()
        if root is not None:
            output.append(root.val)
            if root.right is not None:
                stack.append(root.right)
            if root.left is not None:
                stack.append(root.left)
    return output

def preorderTraversalMorris(root: TreeNode):
    """
    Preorder traversal of tree using Morris traversal where we only keep te output
    Top -> Bottom and Left -> Right
    Time complexity: O(N) -> visit each node (N) once
    Space complexity: O(N) -> depending on structure we can keep the entire tree.
    :param root:
    :return:
    """
    node, output = root, []
    while node:
        if not node.left:
            output.append(node.val)
            node = node.right
        else:
            predecessor = node.left

            while predecessor.right and predecessor.right is not node:
                predecessor = predecessor.right

            if not predecessor.right:
                output.append(node.val)
                predecessor.right = node
                node = node.left
            else:
                predecessor.right = None
                node = node.right
    return output

def inorderTraversal(root: TreeNode):
    """
    Inorder traversal of tree using interations where we push nodes into the output list in the following order:
    Bottom -> Top and Left -> Right
    Time complexity: O(N) -> visit each node (N) once
    Space complexity: O(N) -> depending on structure we can keep the entire tree.
    :param root: (TreeNode Obj) Top of tree.
    :return: Order of analysis
    """
    if root is None:
        return []

    stack, output = [], []

    current = root
    while current or stack:
        while current: # Travel to each node's left child until reach the left leaf
            stack.append(current)
            current = current.left
        current = stack.pop() # Once here this node does not have a left child
        output.append(current.val) # append this node value to our output
        current = current.right # now visit right child

    return output

def postorderTraversal(root: TreeNode):
    """
    Post order traversal of tree using interations where we push nodes into the output list in the following order:
    Bottom -> Top and Left -> Right
    Time complexity: O(N) -> visit each node (N) once
    Space complexity: O(N) -> depending on structure we can keep the entire tree.
    :param root: (TreeNode Obj) Top of tree.
    :return: Order of analysis
    """
    if root is None:
        return []

    stack, output = [(root, False)], []

    while stack:
        node, visted = stack.pop()
        if node:
            if visted:
                output.append(node.val)
            else:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))

    return output


def levelorderTraversal(root: TreeNode):
    """
    Level order traversal of tree using interations where we push nodes into the output list in the following order:
    Bottom -> Top and Left -> Right
    Time complexity: O(N) -> visit each node (N) once
    Space complexity: O(N) -> depending on structure we can keep the entire tree.
    :param root: (TreeNode Obj) Top of tree.
    :return: Order of analysis
    """
    levels = []
    if not root:
        return levels

    level = 0
    queue = deque([root, ])
    while queue:
        levels.append([])
        level_length = len(queue)
        for i in range(level_length):
            node = queue.popleft()

            levels[level].append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        level += 1
    return levels



if __name__ == "__main__":
    #bin_tree_order = [1, None, 2, 3]
    #root = TreeNode(1, None, TreeNode(2, TreeNode(3, None, None), None))
    #print(preorderTraversal(root))
    #print(preorderTraversalMorris(root))
    #print(inorderTraversal(root))
    #print(postorderTraversal(root))
    extended_root = TreeNode(3, TreeNode(9, None, None), TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None)))
    print(levelorderTraversal(extended_root))