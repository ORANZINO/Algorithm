from typing import List

class Solution:
    def process(self, n: int, num_open: int, num_close: int, s: str, ret: List[str]):
        if num_open == n and num_close == n:
            ret.append(s)
            return
        if num_open < n:
            self.process(n, num_open + 1, num_close, s + '(', ret)
        if num_open > num_close:
            self.process(n, num_open, num_close + 1, s + ')', ret)

    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        self.process(n, 0, 0, '', answer)
        return answer

