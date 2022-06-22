T = int(input())
for _ in range(T):
    now = list(input())
    for i in range(len(now) - 1, 0, -1):
        if now[i - 1] < now[i]:
            min_index = i
            for j in range(i + 1, len(now)):
                if now[i - 1] < now[j] < now[min_index]:
                    min_index = j
            now[i - 1], now[min_index] = now[min_index], now[i - 1]
            now = now[:i] + sorted(now[i:])
            break
    print(''.join(now))

