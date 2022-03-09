from typing import List
import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        answer = []

        for i, num in enumerate(nums):
            while q and nums[q[-1]] <= num:
                q.pop()

            q.append(i)

            if q[0] == (i - k):
                q.popleft()

            if i >= (k - 1):
                answer.append(nums[q[0]])

        return answer

