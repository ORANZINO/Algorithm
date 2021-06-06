def solution(s):
    stack = []
    for i in s:
        if not stack: stack.append(i)
        elif i == stack[-1]: stack.pop()
        else: stack.append(i)
    return 0 if stack else 1

"""
스택을 이용하여 짝지어졌을 때 제거하는 방법을 효율적으로 구성할 수 있다.
스택이 애니팡되어 마지막에 다 비었으면 1, 아니면 0
"""