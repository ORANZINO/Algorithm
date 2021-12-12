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



"""
주어진 Linked List를 List화하여 palindrome 여부를 검사.
이 때, pop의 효율성을 위해 deque를 사용하였다.
"""
