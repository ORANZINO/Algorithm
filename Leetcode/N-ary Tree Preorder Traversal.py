from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        stack, answer = [root], []
        
        while stack:
            now = stack.pop()
            if now is None:
                continue
            for i in range(len(now.children) - 1, -1, -1):
                stack.append(now.children[i])
            answer.append(now.val)
        return answer