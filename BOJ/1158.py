n, k = map(int, input().split())
k -= 1
arr = list(range(1, n + 1))
answer = [arr.pop(k)]
temp = k

while arr:
    temp += k
    temp %= len(arr)
    answer.append(arr.pop(temp))

print(f'<{str(answer)[1:-1]}>')