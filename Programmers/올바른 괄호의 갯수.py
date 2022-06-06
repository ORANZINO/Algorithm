answer = 0


def backtrack(now, need_left, need_right):
    if need_left == 0 and need_right == 0:
        global answer
        answer += 1
        return
    if need_left > 0:
        backtrack(now + '(', need_left - 1, need_right)
    if need_right > need_left:
        backtrack(now + ')', need_left, need_right - 1)


def solution(n):
    global answer
    backtrack('', n, n)
    return answer

