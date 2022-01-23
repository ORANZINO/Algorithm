from typing import *


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        answer = []
        def dfs(index, result):
            for i in range(index, len(candidates)):
                temp = sum(result) + candidates[i]
                if temp > target:
                    break
                elif temp < target:
                    dfs(i, result + [candidates[i]])
                else:
                    answer.append(result + [candidates[i]])
        dfs(0, [])
        return answer


"""
itertools의 combinations 모듈을 사용할 수도 있으나 dfs를 사용하여 풀이하자면
하나씩 선택하고 백트래킹 방식으로 가지치기를 수행할 수 있다.
"""