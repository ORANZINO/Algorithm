from collections import deque
from copy import deepcopy

limit = list(map(int, input().split()))
start = [0, 0, limit[2]]
visited = {str(start): True}
ans = [limit[2]]
q = deque()
q.append(start)

while q:
    now = q.popleft()
    for i in range(3):
        if now[i] > 0:
            for j in range(3):
                if i != j:
                    temp = deepcopy(now)
                    if now[i] > (limit[j] - now[j]):
                        temp[i], temp[j] = temp[i] - (limit[j] - temp[j]), limit[j]
                    else:
                        temp[i], temp[j] = 0, temp[j] + temp[i]
                    if str(temp) not in visited:
                        q.append(temp)
                        visited[str(temp)] = True
                        if temp[0] == 0:
                            ans.append(temp[2])

ans.sort()
print(*ans)
