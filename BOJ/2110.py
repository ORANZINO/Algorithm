n, c = map(int, input().split())
house = sorted([int(input()) for _ in range(n)])
start, end = 0, house[-1] - house[0]
result = 0

while start <= end:
    mid = (start + end) // 2
    temp = house[0]
    count = 1
    for i in range(1, n):
        if house[i] - temp >= mid:
            temp = house[i]
            count += 1

    if count >= c:
        result = max(result, mid)
        start = mid + 1
    else:
        end = mid - 1

print(result)

