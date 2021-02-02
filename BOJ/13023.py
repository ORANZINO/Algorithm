import sys

def dfs(k, visited, depth):
    global graph

    visited[k] = True

    for i in graph[k]:
        if not visited[i]:
            if depth == 3:
                return True
            if dfs(i, visited, depth + 1):
                return True
            visited[i] = False
    return False

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
flag = False

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n):
    if dfs(i, [False for _ in range(n)], 0):
        flag = True
        break

print(1 if flag else 0)