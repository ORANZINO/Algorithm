def solution(p):
    def check(s):
        stack = []
        for i in range(len(s)):
            if not stack and s[i] == ')':
                return False
            elif stack and stack[-1] == '(' and s[i] == ')':
                stack.pop()
            else:
                stack.append(s[i])
        return not stack

    def convert(s):
        result = ''
        for char in s:
            if char == '(':
                result += ')'
            else:
                result += '('
        return result

    answer = ''

    for i in range(2, len(p) + 1, 2):
        if p[:i].count('(') == i // 2:
            u, v = p[:i], p[i:]
            if check(u):
                answer = u + solution(v)
            else:
                answer = '(' + solution(v) + ')' + convert(u[1:-1])
            break

    return answer

