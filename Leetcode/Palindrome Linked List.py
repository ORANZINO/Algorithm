from typing import Optional
import collections

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q = collections.deque()

        while head is not None:
            q.append(head.val)
            head = head.next

        while not (len(q) == 0 or len(q) == 1):
            if q.pop() != q.popleft():
                return False
        return True

