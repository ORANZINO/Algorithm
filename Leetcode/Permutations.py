from typing import *

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        def dfs(s, result):
            if not s:
                if result:
                    answer.append(result)
                return
            for i in range(len(s)):
                dfs(s[:i] + s[i + 1:], result + [s[i]])
        dfs(nums, [])
        return answer


