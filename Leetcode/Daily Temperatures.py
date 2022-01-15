from typing import *


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack, output = [], [0] * len(temperatures)
        for i, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                j = stack.pop()
                output[j] = i - j
            stack.append(i)
        return output


"""
현재 temperature는 이전 temperature에 비해 더 크거나 / 작거나 같을 것이다.
stack에 작거나 같을 때마다 쌓다보면 stack은 reverse로 sort된 형태를 가지게 된다.
그러므로 더 큰 temperature가 등장했다면 stack을 계속 pop해주는 방식을 취하면 된다.
pop할 때, 서로의 index 차이를 output에 기록한다.
"""