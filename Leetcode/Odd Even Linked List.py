from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        odd = head
        even = head.next
        even_head = head.next
        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next
        odd.next = even_head
        return head


"""
홀수 노드와 짝수 노드들끼리 분리해서 재정렬한 뒤 짝수 노드의 첫 노드을 홀수 노드의 마지막 노드와 연결시킨다.
"""