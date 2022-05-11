from typing import List, Optional
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q, answer, now_level, temp = collections.deque(), [[root.val]], 0, []
        q.append((root, 0))

        while q:
            now, level = q.popleft()
            if level > now_level:
                answer.append(temp)
                temp, now_level = [], level
            if now.left:
                q.append((now.left, level + 1))
                temp.append(now.left.val)
            if now.right:
                q.append((now.right, level + 1))
                temp.append(now.right.val)
        return answer[::-1]