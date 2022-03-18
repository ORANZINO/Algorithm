from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [int(expression)]
        result = []
        for i, char in enumerate(expression):
            if char in "-*+":
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                for l in left:
                    for r in right:
                        result.append(eval(f'{l}{char}{r}'))
        return result

