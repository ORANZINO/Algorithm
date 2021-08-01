from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        water = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max, right_max = max(left_max, height[left]), max(right_max, height[right])

            if left_max <= right_max:
                water += left_max - height[left]
                left += 1
            else:
                water += right_max - height[right]
                right -= 1
        return water


"""
투 포인터 방식의 문제
왼쪽과 오른쪽의 height_max값을 지속적으로 업데이트해나가며 더 작은 쪽에
확신적으로 물을 채워나가며 서로의 간격을 좁힌다.
"""