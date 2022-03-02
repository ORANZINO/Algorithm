from typing import *


class Solution:
    # 제출용
    # def search(self, nums: List[int], target: int) -> int:
    #     try:
    #         return nums.index(target)
    #     except:
    #         return -1

    # Binary Search
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + (right - left)) // 2
            if nums[mid] > right:
                left = mid + 1
            else:
                right = mid
        pivot = left

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + (right - left)) // 2
            mid_pivot = (mid + pivot) % len(nums)

            if nums[mid_pivot] < target:
                left = mid + 1
            elif nums[mid_pivot] > target:
                right = mid - 1
            else:
                return mid_pivot
        return -1

'''
O(log n) 안에 풀라고 해놓고 구현하면 시간초과 뜬다...;
일단 제출은 index 내장함수 써서 했다.
가장 작은 수인 pivot을 찾는 데에 binary search를 쓴 점이 인상적이었다.
우상향하는 구간의 가장 작은 인덱스를 left가 가리키도록 설계되었다.
그 이후에는 pivot만큼을 더하여 이진탐색으로 답을 찾는다.
'''
