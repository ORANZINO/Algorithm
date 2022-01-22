from typing import *
import itertools


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return [c for i in range(len(nums) + 1) for c in itertools.combinations(nums, i)]


