from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum_val = nums[i] + nums[left] + nums[right]
                if sum_val < 0:
                    left += 1
                elif sum_val > 0:
                    right -= 1
                else:
                    results.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return results


"""
모든 수에 대해 (중복 제외)
합쳐서 0이 되는 나머지 두 수를 찾을 수 있도록 하기 위해 투 포인터 알고리즘을 사용한다.
"""