h, w = map(int, input().split())
block = [[False] * w for _ in range(h)]
height = list(map(int, input().split()))
for i, ht in enumerate(height):
    for j in range(ht):
        block[j][i] = True

i, count = 0, 0
ans = 0
start, end = False, False
while not (start and end):
    temp = 0
    count = 0
    for j in range(1, w):
        if temp == 0 and block[i][j - 1] and not block[i][j]:
            temp = 1
        elif temp != 0 and not block[i][j]:
            temp += 1
        elif temp > 0 and block[i][j]:
            count += temp
            temp = 0
    if not start and count > 0:
        start  = True
    if start and count == 0:
        end = True
    ans += count
    i += 1
    if i == h:
        break
print(ans)
