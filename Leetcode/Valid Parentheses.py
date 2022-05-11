class Solution:
    def isValid(self, s: str) -> bool:
        pair_dic = {')': '(', '}': '{', ']': '['}
        stack = []
        for c in s:
            if c in pair_dic and stack and stack[-1] == pair_dic[c]:
                stack.pop()
            else:
                stack.append(c)
        return not bool(stack)

