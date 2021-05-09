def separate(x):
    max_val, min_val = arr[0], arr[0]
    count = 1
    for i in range(1, len(arr)):
        max_val = max(max_val, arr[i])
        min_val = min(min_val, arr[i])
        if (max_val - min_val) > x:
            count += 1
            max_val = arr[i]
            min_val = arr[i]
    return count


n, m = map(int, input().split())
arr = list(map(int, input().split()))
start, end = 0, max(arr)


while start <= end:
    mid = (start + end) // 2
    if separate(mid) <= m:
        end = mid - 1
        ans = mid
    else:
        start = mid + 1

print(ans)
