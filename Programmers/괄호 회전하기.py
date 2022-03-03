from collections import defaultdict

def solution(s):
    answer = 0
    pairs = defaultdict(str)
    pairs[']'], pairs[')'], pairs['}'] = '[', '(', '{'
    for i in range(len(s)):
        stack = []
        for j in range(len(s)):
            j = (i + j) % len(s)
            if stack and stack[-1] == pairs[s[j]]:
                stack.pop()
            else:
                stack.append(s[j])
        if not stack:
            answer += 1
    return answer

