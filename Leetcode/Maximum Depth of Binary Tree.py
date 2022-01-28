from typing import *
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = collections.deque()
        q.append((root, 1))
        answer = 0
        if root:
            while q:
                node, depth = q.popleft()
                answer = max(answer, depth)
                if node.right:
                    q.append((node.right, depth + 1))
                if node.left:
                    q.append((node.left, depth + 1))
        return answer