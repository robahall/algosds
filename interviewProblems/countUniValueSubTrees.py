class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def countUnivalSubtrees(root: TreeNode) -> int:
    """
    Finish
    Time Complexity O(N)
    Space Complexity O(log(N)) to O(N)
    :param root:
    :param sum:
    :return:
    """
    answer = 0
    def recuse(node, parent, answer):
        if not node:
            return True
        left = recuse(node.left, node.val, answer)
        right = recuse(node.right, node.val, answer)
        if left and right:
            answer += 1
        return left and right and node.val == parent

    recuse(root, None, answer)
    return answer




if __name__ == "__main__":
    tree = TreeNode(5, TreeNode(1, TreeNode(5), TreeNode(5)), TreeNode(5, None, TreeNode(5)))
    print(countUnivalSubtrees(tree))