from typing import *

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if all(num == 0 for num in nums):
            return "0"
        return ''.join(sorted([str(num) for num in nums], reverse=True, key=lambda x: x * 10))

