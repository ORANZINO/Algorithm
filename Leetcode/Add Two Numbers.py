from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def toReversedList(self, head: ListNode) -> ListNode:
        result = []
        while head:
            result.insert(0, head.val)
            head = head.next
        return result
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1, l2 = self.toReversedList(l1), self.toReversedList(l2)
        temp = str(int(''.join(map(str, l1))) + int(''.join(map(str, l2))))
        prev: ListNode = None
        for t in temp:
            node = ListNode(t)
            node.next = prev
            prev = node
        return node



"""
주어진 linked list를 반대 순서인 list로 변환한다
각 리스트가 나타내는 숫자들을 더해준다.
해당 숫자들을 다시 반대 순서인 linked list로 변환한다
"""