from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 병합정렬 사용하는 방법

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode):
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next):
            return head
        half, slow, fast = None, head, head
        while fast and fast.next:
            half, slow, fast = slow, slow.next, fast.next.next
        half.next = None
        head, slow = self.sortList(head), self.sortList(slow)
        return self.mergeTwoLists(head, slow)


# 내장 함수 사용하는 방법


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        lst: List = []
        while p:
            lst.append(p.val)
            p = p.next

        lst.sort()

        p = head
        for i in range(len(lst)):
            p.val = lst[i]
            p = p.next

        return head


'''
1번 방법은 병합정렬 기법을 사용한다. Linked List를 반으로 나누기 위해 런너를 사용한다.
2번 방법은 파이썬에 내장된 sort함수를 사용한다. 쉽고 직관적이지만 면접에서는 까일 것 같은 방법이랄까?
'''