import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)
        missing = len(t)
        left, start, end = 0, 0, 0
        flag = False

        for right, char in enumerate(s):
            missing -= (need[char] > 0)
            need[char] -= 1

            if missing == 0:
                while left <= right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1

                if not end or (right - left) < (end - start):
                    flag = True
                    start, end = left, right
                need[s[left]] += 1
                missing += 1
                left += 1

        return s[start:end + 1] if flag else ""

