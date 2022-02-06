from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if node:
                dfs(node.left)
                dfs(node.right)
                node.left, node.right = node.right, node.left
        dfs(root)
        return root


"""
dfs 방식으로 모든 노드의 left와 right를 swap한다.
"""