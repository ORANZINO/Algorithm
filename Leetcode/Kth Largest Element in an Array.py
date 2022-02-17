from typing import *
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]


'''
heap을 이용하여 단순하게 해결하였다
'''