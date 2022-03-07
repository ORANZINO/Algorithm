from typing import List
import bisect

class Solution:
    # 이진 탐색 직접 구현
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers) - 1):
            if numbers[i] == numbers[i + 1]:
                if numbers[i] * 2 == target:
                    return [i + 1, i + 2]
                else:
                    continue
            now_target = target - numbers[i]
            left, right = i + 1, len(numbers) - 1
            while left <= right:
                mid = (left + right) // 2
                if numbers[mid] < now_target:
                    left = mid + 1
                elif numbers[mid] > now_target:
                    right = mid - 1
                else:
                    return [i + 1, mid + 1]

    # bisect 모듈 이용
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            expected = target - v
            i = bisect.bisect_left(numbers, expected, k + 1)
            if i < len(numbers) and numbers[i] == expected:
                return [k + 1, i + 1]