# DFS

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

k = int(input())

def dfs(v, num):
    global visited
    global graph

    visited[v] = num
    for adj in graph[v]:
        if visited[adj] == 0:
            dfs(adj, -num)


for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    visited = [0 for _ in range(v + 1)]

    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, v + 1):
        if visited[i] == 0:
            dfs(i, 1)

    print("YES" if all(all(visited[i] == -visited[j] for j in graph[i]) for i in range(1, v + 1)) else "NO")

#BFS

from collections import deque
import sys
input = sys.stdin.readline

def bfs(v):
    visited[v] = 1
    q = deque([v])

    while q:
        temp = q.popleft()
        for adj in graph[temp]:
            if visited[adj] == 0:
                visited[adj] = -visited[temp]
                q.append(adj)
            elif visited[adj] == visited[temp]:
                return False
    return True

k = int(input())

for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    visited = [0 for _ in range(v + 1)]
    flag = True

    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, v + 1):
        if visited[i] == 0:
            if not bfs(i):
                flag = False
                break

    print("YES" if flag else "NO")