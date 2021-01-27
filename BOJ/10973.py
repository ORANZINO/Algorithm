n = int(input())
target = list(map(int, input().split()))
i = n - 2

while 0 <= i:
    if target[i] > target[i + 1]:
        break
    else:
        i -= 1

if i == -1:
    print(-1)
else:
    j = n - 1
    while i < j:
        if target[i] > target[j]:
            target[i], target[j] = target[j], target[i]
            print(' '.join(map(str, (target[:i + 1] + sorted(target[i + 1:], reverse=True)))))
            break
        else:
            j -= 1
