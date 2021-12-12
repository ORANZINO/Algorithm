from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node, prev = head, None

        while node:
            daum, node.next = node.next, prev
            node, prev = daum, node

        return prev


"""
Linked List를 Reverse하는 문제.
Linked List를 travese하며 link들의 방향을 모두 바꾸어주는 방식으로 구현했다.
"""
