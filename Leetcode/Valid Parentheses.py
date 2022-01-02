class Solution:
    def isValid(self, s: str) -> bool:
        pair_dic = {')': '(', '}': '{', ']': '['}
        stack = []
        for c in s:
            if stack and stack[-1] == pair_dic[c]:
                stack.pop()
            else:
                stack.append(c)
        return True if not stack else False

