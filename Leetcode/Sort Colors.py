from typing import *

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red, white, blue = 0, 0, len(nums)

        while white < blue:
            if nums[white] < 1:
                nums[red], nums[white] = nums[white], nums[red]
                red += 1
                white += 1
            elif nums[white] > 1:
                blue -= 1
                nums[white], nums[blue] = nums[blue], nums[white]
            else:
                white += 1


'''
3종류의 원소로 이루어진 배열을 정렬한다.
가장 작은 수와 가장 큰 수를 오른쪽부터 채워나가고 이외에는 그냥 놔두는 방식.
'''