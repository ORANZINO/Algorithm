from math import ceil

def solution(n, stations, w):
    before = 1
    arr = []
    for s in stations:
        if s - w > before:
            arr.append(s - w - before)
        before = s + w + 1
    if before <= n:
        arr.append(n - before + 1)
    return sum(ceil(a / (2 * w + 1)) for a in arr)

