from typing import *

# 삽입 정렬을 이용한 방법

class Solution:
    @staticmethod
    def to_swap(s1: str, s2: str):
        return s1 + s2 > s2 + s1

    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        for i in range(1, len(nums)):
            for j in range(i, 0, -1):
                if self.to_swap(nums[j], nums[j - 1]):
                    nums[j], nums[j - 1] = nums[j - 1], nums[j]
                else:
                    break
        return str(eval(''.join(nums)))


# 사전식 정렬을 이용한 방법
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if all(num == 0 for num in nums):
            return "0"
        return ''.join(sorted([str(num) for num in nums], reverse=True, key=lambda x: x * 10))


'''
정렬의 기준을 어떻게 잡을 것인지에 대한 문제이다. 
삽입 정렬은 concatenate했을 때 더 커지는 것을 기준으로 정렬하게 한다.
sorted()를 쓴 방법은 해당 수를 반복하여 숫자의 길이에 상관없이 비교할 수 있도록 하여 정렬한다.
'''

