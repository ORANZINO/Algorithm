from collections import defaultdict


def solution(n, results):
    win, lose = defaultdict(set), defaultdict(set)

    for a, b in results:
        win[a].add(b)
        lose[b].add(a)

    for i in range(1, n + 1):
        for w in win[i]:
            lose[w] |= lose[i]
        for l in lose[i]:
            win[l] |= win[i]

    return sum(len(win[i]) + len(lose[i]) == (n - 1) for i in range(1, n + 1))

