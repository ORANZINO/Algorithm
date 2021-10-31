from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        temp = 1

        for i in range(len(nums)):
            answer.append(temp)
            temp *= nums[i]

        temp = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= temp
            temp *= nums[i]

        return answer


"""
전체 곱에 나눗셈을 하는 것이 허용되지 않으므로 그냥
자신의 양쪽에 있는 수들을 곱하는 방식으로 하면 된다. 왼쪽 항들을 곱한 array를 만들어
각 항에 다시 오른족 항들을 곱한 수를 곱해주면 완성!
"""