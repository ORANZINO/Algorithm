from typing import *
import bisect

class Solution:
    # recursion
    # def search(self, nums: List[int], target: int) -> int:
    #     def binary_search(left, right):
    #         if left <= right:
    #             mid = (left + right) // 2
    #
    #             if nums[mid] < target:
    #                 return binary_search(mid + 1, right)
    #             elif nums[mid] > target:
    #                 return binary_search(left, mid - 1)
    #             else:
    #                 return mid
    #         else:
    #             return -1
    #
    #     return binary_search(0, len(nums) - 1)

    # while loop
    # def search(self, nums: List[int], target: int) -> int:
    #     left, right = 0, len(nums) - 1
    #     while left <= right:
    #         mid = (left + right) // 2
    #         if nums[mid] < target:
    #             left = mid + 1
    #         elif nums[mid] > target:
    #             right = mid - 1
    #         else:
    #             return mid
    #     return -1

    # 모듈 사용
    def search(self, nums: List[int], target: int) -> int:
        answer = bisect.bisect_left(nums, target)
        return answer if answer < len(nums) and nums[answer] == target else -1