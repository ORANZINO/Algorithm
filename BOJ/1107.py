nums = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
n = int(input())
m = int(input())
if m:
    broken = set(input().split())
    nums -= broken
ans = abs(n - 100)


if nums:
    i = 0
    while True:
        left = 0 if n - i <= 0 else n - i
        right = n + i
        left_flag = all(l in nums for l in str(left))
        right_flag = all(l in nums for l in str(right))
        if left_flag or right_flag:
            if left_flag:
                ans = min(ans, i + len(str(left)))
            if right_flag:
                ans = min(ans, i + len(str(right)))
            break
        i += 1
print(ans)
