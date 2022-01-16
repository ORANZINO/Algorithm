class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = result = ListNode(None)
        heap = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i],))
        while heap:
            _, i, result.next = heapq.heappop(heap)
            result = result.next
            if result.next:
                heapq.heappush(heap, (result.next.val, i, result.next))
        return root.next