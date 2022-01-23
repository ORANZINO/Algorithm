from typing import *
import itertools


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return [c for i in range(len(nums) + 1) for c in itertools.combinations(nums, i)]


"""
combinations 모듈로 모든 가짓수의 조합을 구해 부분집합을 다 구했다.
"""