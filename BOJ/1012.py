def dfs(coordinates, graph, visited):
    steps = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    x, y = coordinates
    visited[x][y] = True
    for step in steps:
        i = x + step[0]
        j = y + step[1]
        if (0 <= i < len(graph)) and (0 <= j < len(graph[0])):
            if graph[i][j] and not visited[i][j]:
                dfs((i, j), graph, visited)

t = int(input())
for _ in range(t):
    answer = 0
    m, n, k = map(int, input().split())
    field = [[0] * n for _ in range(m)]
    visited = [[False] * n for _ in range(m)]
    for _ in range(k):
        x, y = map(int, input().split())
        field[x][y] = 1
    for i in range(m):
        for j in range(n):
            if field[i][j] and not visited[i][j]:
                dfs((i, j), field, visited)
                answer += 1
    print(answer)
    
# 지렁이를 발견하면 dfs를 수행해서 해당 영역 
