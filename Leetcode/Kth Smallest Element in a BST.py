from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.k = 0
        self.i = 0
        self.ret = 0

    def inorder(self, node: Optional[TreeNode]):
        if node is None:
            return False
        ret = self.inorder(node.left)
        if ret:
            return True
        self.i += 1
        if self.i == self.k:
            self.ret = node.val
            return True
        return self.inorder(node.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.inorder(root)
        return self.ret