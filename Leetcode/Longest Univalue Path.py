from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    longest: int = 0

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0
            self.longest = max(self.longest, left + right)
            return max(left, right)

        dfs(root)
        return self.longest

"""
리프 노드들의 차수는 기본적으로 1이다.
그 위로 올라가면서 부모 노드들은 자식 노드와 값이 같다면 해당 자식 노드의 차수 + 1한 값을 자신의 차수로 가진다.
이렇게 계산하여 한 node에서 자식 노드들의 차수를 더한 값의 최댓값을 답으로 도출할 수 있다.
"""