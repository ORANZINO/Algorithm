from typing import Optional
import collections

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        q, answer = collections.deque(), 0
        q.append((root, False))
        while q:
            node, left = q.popleft()
            if left and node.left is None and node.right is None:
                answer += node.val
            if node.left:
                q.append((node.left, True))
            if node.right:
                q.append((node.right, False))
        return answer


