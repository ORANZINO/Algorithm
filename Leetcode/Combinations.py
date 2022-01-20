from typing import *

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = list(range(1, n + 1))
        answer = []
        def dfs(x, count, result):
            if count == 0:
                if result:
                    answer.append(result)
                return
            for i in range(len(x) - count + 1):
                dfs(x[i + 1:], count - 1, result + [x[i]])
        dfs(range(1, n + 1), k, [])
        return answer