from typing import List

class Solution:
    # Divide And Conquer
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]

        half = len(nums) // 2
        a = self.majorityElement(nums[:half])
        b = self.majorityElement(nums[half:])

        return [b, a][nums.count(a) > len(nums) // 2]

    # Pythonic
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]

