from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])

"""
정렬해서 두 수씩 묶는 것이 최적.
그렇기에 그냥 정렬해서 짝수번째 항들의 합을 구해도 된다.
"""
