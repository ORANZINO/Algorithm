def solution(n, s, a, b, fares):
    INF = int(1e9)
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        graph[i][i] = 0
    for c, d, f in fares:
        graph[c][d] = graph[d][c] = f

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

    return min(graph[s][i] + graph[i][a] + graph[i][b] for i in range(1, n + 1))
