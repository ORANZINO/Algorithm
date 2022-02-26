from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = parent = ListNode(0)
        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next

            cur.next, head.next, head = head, cur.next, head.next

            if head and cur.val > head.val:
                cur = parent
        return parent.next


'''
삽입 정렬을 사용하되, Linked List에서 순차탐색하며 삽입할 곳을 찾기 위해 
계속 첫 엘리멘트를 가리키는 parent를 필요로 한다.
다만 원래 큰 수에서부터 거꾸로 탐색하는 기존의 삽입 정렬 방식을 할 수 없으므로 효율성이 줄어든다.
이에 따라 cur의 val이 head보다 커서 앞으로 돌아갈 필요성이 있을 때에만 처음으로 돌아가도록 하면 효율성을 높일 수 있다. 
'''