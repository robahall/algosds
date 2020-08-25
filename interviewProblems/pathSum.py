class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root: TreeNode, sum: int) -> bool:
    """
    Top Down recursion of tree
    Time Complexity O(N)
    Space Complexity O(log(N)) to O(N)
    :param root:
    :param sum:
    :return:
    """

    if not root:
        return False
    sum -= root.val
    if not root.left and not root.right:
        return sum == 0
    return hasPathSum(root.left, sum) or hasPathSum(root.right, sum)



if __name__ == "__main__":
    tree = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(1))))
    print(hasPathSum(tree, 22))

    #sum = 22 return True since 5->4->11->2