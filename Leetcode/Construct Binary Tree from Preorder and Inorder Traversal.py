from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            k = inorder.index(preorder[0])
            root = TreeNode(preorder[0], self.buildTree(preorder[1:k+1], inorder[:k]), self.buildTree(preorder[k+1:], inorder[k+1:]))
            return root


'''
Preorder의 첫 번째 수는 언제나 root가 되므로 inorder에서 좌우를 구분짓는 것이 가능하다.
이를 이용하여 recursion으로 문제를 해결하였다.
'''