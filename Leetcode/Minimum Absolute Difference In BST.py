from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorder(self, node, ret):
        if node is None:
            return
        self.inorder(node.left, ret)
        ret.append(node.val)
        self.inorder(node.right, ret)

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        sorted_arr = []
        self.inorder(root, sorted_arr)
        return min(sorted_arr[i] - sorted_arr[i - 1] for i in range(1, len(sorted_arr)))

