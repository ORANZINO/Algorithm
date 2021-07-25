from collections import deque


def solution(s):
    if len(s) % 2 == 1 or s[0] == ')':
        return False
    s = deque(list(s))
    k = deque()
    while s:
        if s[0] == '(':
            k.append(s.popleft())
        elif len(k) == 0:
            return False
        elif k[-1] == '(':
            k.pop()
            s.popleft()
        else:
            return False
    return len(k) == 0

"""
stack 구조를 활용하여 푸는 문제
() 쌍이 맞으면 둘 다 pop하는 식으로 해결한다.
쌍이 맞을 수 없는 경우, stack이 남는 경우, 빈 스택에 ')'가 들어오는 경우를 예외처리하였다.
"""