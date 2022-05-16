from typing import Optional
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        n = 2 ** 31
        q = collections.deque()
        q.append((root, -n - 1, n))
        while q:
            temp, min_val, max_val = q.popleft()
            if temp.left:
                left_max = min(max_val, temp.val)
                if not (min_val < temp.left.val < left_max):
                    return False
                q.append((temp.left, min_val, left_max))
            if temp.right:
                right_min = max(min_val, temp.val)
                if not (right_min < temp.right.val < max_val):
                    return False
                q.append((temp.right, right_min, max_val))
        return True