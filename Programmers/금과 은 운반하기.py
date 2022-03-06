def solution(a, b, g, s, w, t):
    answer = int(1e9) * int(1e5) * 4
    start, end = 0, int(1e9) * int(1e5) * 4

    while start <= end:
        mid = (start + end) // 2
        gold, silver, total = 0, 0, 0
        for i in range(len(g)):
            move_count = mid // (2 * t[i])
            if mid % (2 * t[i]) >= t[i]:
                move_count += 1
            gold += min(move_count * w[i], g[i])
            silver += min(move_count * w[i], s[i])
            total += min(move_count * w[i], g[i] + s[i])
        if gold >= a and silver >= b and total >= a + b:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
    return answer

