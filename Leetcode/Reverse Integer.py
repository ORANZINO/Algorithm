class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        minus = False
        if int(x) < 0:
            minus = True
            x = x[1:]
        x = int(x[::-1])
        if x < -(2 ** 31) or x >= (2 ** 31):
            return 0
        return -x if minus else x

"""
string으로 바꿔서 뒤집어주되, 음수일 경우와 지정된 범위를 넘어설 경우 예외처리를 해주는 방식
"""