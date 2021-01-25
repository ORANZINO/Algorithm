import sys

input = sys.stdin.readline

def dfs(k, temp, r, c):
    global n, m
    global array
    global answer
    global visited
    global max_val

    steps = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    if k == 4:
        answer = max(answer, temp)
        return
    if temp + (4 - k) * max_val < answer:
        return
    for step in steps:
        next_r = r + step[0]
        next_c = c + step[1]
        if 0 <= next_r < n and 0 <= next_c < m:
            if not visited[next_r][next_c]:
                visited[next_r][next_c] = True
                if k == 2:
                    dfs(k + 1, temp + array[next_r][next_c], r, c)
                dfs(k + 1, temp + array[next_r][next_c], next_r, next_c)
                visited[next_r][next_c] = False
    return


n, m = map(int, input().split())
array = []
answer = 0
visited = [[False for _ in range(m)] for _ in range(n)]

for _ in range(n):
    array.append(list(map(int, input().split())))

max_val = max(map(max, array))

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(1, array[i][j], i, j)
        visited[i][j] = False

print(answer)

