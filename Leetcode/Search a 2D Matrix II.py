from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        row, col = 0, len(matrix[0]) - 1

        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row += 1
            else:
                col -= 1
        return False

    # Pythonic
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return any(target in row for row in matrix)

'''
2가지 방법으로 해결
1. 행렬의 특성을 살려 원하는 값보다 작을 때는 행을, 클 때는 열을 움직여 탐색
2. Pythonic하게 any로 모든 row 검사
'''