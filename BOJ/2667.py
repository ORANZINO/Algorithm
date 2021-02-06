from collections import deque

n = int(input())
house = []
visited = [[False] * n for _ in range(n)]
steps = [(1, 0), (0, 1), (-1, 0), (0, -1)]
complex_count = 0
house_count = []

for _ in range(n):
    house.append(list(map(int, input())))

for i in range(n):
    for j in range(n):
        if house[i][j] and not visited[i][j]:
            q = deque([(i, j)])
            visited[i][j] = True
            count = 1
            while q:
                temp = q.popleft()
                for step in steps:
                    x, y = temp[0] + step[0], temp[1] + step[1]
                    if 0 <= x < n and 0 <= y < n:
                        if house[x][y] and not visited[x][y]:
                            q.append((x, y))
                            visited[x][y] = True
                            count += 1
            house_count.append(count)
            complex_count += 1
print(complex_count)
print(*sorted(house_count), sep='\n')
