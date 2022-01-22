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


    