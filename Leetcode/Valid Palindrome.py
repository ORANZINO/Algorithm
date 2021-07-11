import collections
import re

# 1st solution

class Solution:
    def isPalindrome(self, s: str) -> bool:
        q = collections.deque()

        for c in s:
            if c.isalnum():
                q.append(c.lower())

        while len(q) > 1:
            if q.popleft() != q.pop():
                return False

        return True

"""
문자열 전처리 과정에서 isalnum()을 사용하여 각 character를 검사하고,
Deque를 이용하여 양쪽의 character를 차례로 검사하며 palindrome을 체크한다.
"""

# 2nd Solution

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1]

"""
문자열 전처리 과정에서 정규식을 사용하여 필요없는 character들을 걸러내고,
슬라이싱을 이용하여 한 번에 palindrome을 체크한다.
"""