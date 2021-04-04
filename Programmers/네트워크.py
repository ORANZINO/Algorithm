from collections import deque

def solution(n, computers):
    q = deque([0])
    visited = [False] * n
    answer = 0
    for i in range(n):
        if not visited[i]:
            q = deque([i])
            answer += 1
            while q:
                v = q.popleft()
                if not visited[v]:
                    visited[v] = True
                    for j in range(n):
                        if computers[v][j]:
                            q.append(j)
    return answer
