from collections import defaultdict
from itertools import product

def solution(board):
    n, answer = len(board), 0
    highest = [n] * n
    loc = defaultdict(list)
    needed = dict()
    board.append([1] * n)
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                loc[board[i][j]].append((i, j))
                if highest[j] == n:
                    highest[j] = i
    for key in loc:
        x_counter, y_counter = defaultdict(int), defaultdict(int)
        for x, y in loc[key]:
            x_counter[x] += 1
            y_counter[y] += 1
        x_arr = [x for x in x_counter if x_counter[x] == 1]
        y_arr = [y for y in y_counter if y_counter[y] == 1]
        needed[key] = list(product(x_arr, y_arr))
    flag = 1
    while flag and needed:
        flag = 0
        for key in needed:
            if all(highest[y] > x for x, y in needed[key]):
                flag = key
                for x, y in loc[key]:
                    board[x][y] = 0
                    for k in range(n + 1):
                        if board[k][y] != 0:
                            highest[y] = k
                            break
                answer += 1
                break
        if flag:
            del needed[flag]
    return answer