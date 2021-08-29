from collections import deque


def solution(N, road, K):
    INF = int(1e9)
    graph = [[INF] * (N + 1) for _ in range(N + 1)]
    for r in road:
        graph[r[0]][r[1]] = min(graph[r[0]][r[1]], r[2])
        graph[r[1]][r[0]] = min(graph[r[0]][r[1]], r[2])
    distance = [INF] * (N + 1)
    q = deque()
    q.append((1, 0))
    distance[1] = 0
    while q:
        e, dist = q.popleft()
        if dist > K:
            continue
        for i in range(2, N + 1):
            temp = dist + graph[e][i]
            if temp < distance[i] and temp <= K:
                q.append((i, temp))
                distance[i] = temp
    return (N + 1) - distance.count(INF)


"""
BFS를 사용해서 1부터 다른 점까지의 거리를 모두 구한다.
"""

