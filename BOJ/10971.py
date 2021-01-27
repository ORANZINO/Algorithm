def search(now, visited, result, k):
    global answer
    global graph
    global n

    if (k == n) and (graph[now][0] != 0):
        answer = min(answer, result + graph[now][0])
        return
    for i in range(n):
        if (not visited[i]) and (graph[now][i] != 0):
            visited[i] = True
            search(i, visited, result + graph[now][i], k + 1)
            visited[i] = False

INF = int(1e9)
n = int(input())
graph = []
visited = [False] * n

for _ in range(n):
    graph.append(list(map(int, input().split())))

answer = INF

visited[0] = True
search(0, visited, 0, 1)

print(answer)