from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(nums):
            if target - num in dic:
                return [i, dic[target - num]]
            dic[num] = i

"""
dictionary에 넣어서 해싱 방법으로 나머지 수를 찾는 데에 걸리는 시간을 줄였다.
또한, 확인할 때마다 dictionary를 업데이트함으로써 loop의 개수를 줄였다.
"""