from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        answer = []
        dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        def dfs(s, result):
            if not s:
                if result:
                    answer.append(result)
                return

            for char in dic[s[0]]:
                dfs(s[1:], result + char)

        dfs(digits, '')

        return answer

"""
가능한 경우를 dfs로 모두 알아낼 수 있다.
"""