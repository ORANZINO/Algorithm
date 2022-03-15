from typing import *

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        j, count = 0, 0
        for i in range(len(g)):
            while j < len(s) and s[j] < g[i]:
                j += 1
            if j == len(s):
                break
            else:
                count += 1
                j += 1
        return count