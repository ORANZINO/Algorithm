from collections import deque
INF = int(1e9)


def bfs(q):
    steps = [(1, 0), (0, 1), (-1, 0), (0, - 1)]
    while q:
        a, b, w = q.popleft()
        if a == (n - 1) and b == (m - 1):
            return distance[n - 1][m - 1][w]
        for step in steps:
            x = a + step[0]
            y = b + step[1]
            if 0 <= x < n and 0 <= y < m:
                if distance[x][y][w] == INF and graph[x][y] == 0:
                    distance[x][y][w] = distance[a][b][w] + 1
                    q.append([x, y, w])
                elif distance[x][y][w] == INF and graph[x][y] == 1 and w == 1:
                    distance[x][y][0] = distance[a][b][w] + 1
                    q.append([x, y, 0])
    return -1


n, m = map(int, input().split())
graph = []
distance = [[[INF, INF] for _ in range(m)] for _ in range(n)]
distance[0][0][1] = 1
for _ in range(n):
    graph.append(list(map(int, list(input()))))

q = deque()
q.append([0, 0, 1])
print(bfs(q))

