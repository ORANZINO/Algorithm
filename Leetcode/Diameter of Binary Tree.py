from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    longest: int = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return -1
            left = dfs(node.left)
            right = dfs(node.right)
            self.longest = max(self.longest, left + right + 2)

            return max(left, right) + 1

        dfs(root)
        return self.longest


"""
리프 노드의 차수는 0이며, 그 이외의 노드들의 차수는 자식 노드의 차수 최댓값 + 1이다.
최대 거리는 자식 노드들의 차수를 더한 값에 2를 더한 값이다.
이러한 원리를 바탕으로 DFS를 수행하여 답을 얻어낼 수 있다. 
"""

