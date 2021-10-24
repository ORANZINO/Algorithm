from math import ceil

def solution(n, words):
    stack = []
    for i, word in enumerate(words):
        if len(stack) == 0 or (word not in stack and stack[-1][-1] == word[0]):
            stack.append(word)
        else:
            return i % n + 1, ceil((i + 1) / n)
    return 0, 0


"""
끝말잇기가 성립하지 않을 때 그 사람의 번호와 순서를 리턴
쭉 성립했으면 0,0 리턴
"""