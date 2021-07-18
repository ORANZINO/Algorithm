class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''

        for i in range(len(s) - 1):
            result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)

        return result

"""
중심 문자열에서 투 포인터로 하나씩 확장해나가며 longest palindrome을 찾는다.
이 때, 짝수 palindrome이랑 홀수 palindrome을 모두 고려할 수 있도록 해야한다.
알게된 점: max() 함수에서 key를 사용할 수 있는 것
"""