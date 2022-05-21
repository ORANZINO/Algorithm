def solution(s):
    if s == s[::-1]:
        return len(s)
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    return max(max(expand(i, i + 1), expand(i, i + 2)) for i in range(len(s) - 1))

