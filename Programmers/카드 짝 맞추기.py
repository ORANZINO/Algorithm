from collections import deque, defaultdict
from itertools import permutations, product
from copy import deepcopy


def check(x, y):
    return 0 <= x < 4 and 0 <= y < 4


def convert(x):
    return 3 if x == 1 else 0


def distance(board, r, c, order):
    result, steps = 0, [(1, 0), (0, 1), (-1, 0), (0, -1)]
    prev = []
    for i, p in enumerate(order):
        x, y = p
        q, visited = deque(), [[False] * 4 for _ in range(4)]
        visited[r][c] = True
        q.append((r, c, 0))
        while_flag = False
        while q:
            a, b, dist = q.popleft()
            for step in steps:
                na, nb = a + step[0], b + step[1]
                if check(na, nb) and not visited[na][nb]:
                    if na == x and nb == y:
                        result += dist + 1
                        while_flag = True
                        break
                    q.append((na, nb, dist + 1))
                    visited[na][nb] = True
                flag = False
                if check(na, nb):
                    if step[0] != 0:
                        while not board[na][nb] and na != convert(step[0]):
                            na, flag = na + step[0], True
                    else:
                        while not board[na][nb] and nb != convert(step[1]):
                            nb, flag = nb + step[1], True
                    if flag and not visited[na][nb]:
                        if na == x and nb == y:
                            result += dist + 1
                            while_flag = True
                            break
                        q.append((na, nb, dist + 1))
                        visited[na][nb] = True
            if while_flag:
                break
        r, c = x, y
        if prev:
            board[r][c] = board[prev[0]][prev[1]] = 0
            prev = []
        else:
            prev.append(r)
            prev.append(c)
    return result


def solution(board, r, c):
    dic, answer = defaultdict(list), []
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                dic[board[i][j]].append((i, j))
    for key in dic:
        dic[key] = list(permutations(dic[key], 2))
    for p in permutations(dic.values(), len(dic)):
        for q in product(*p):
            answer.append(distance(deepcopy(board), r, c, [b for a in q for b in a]))
    return min(answer) + len(dic) * 2

