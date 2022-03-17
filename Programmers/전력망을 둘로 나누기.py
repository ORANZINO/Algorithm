from collections import deque


def solution(n, wires):
    graph = [[] for _ in range(n)]
    answer = n
    for a, b in wires:
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    for a, b in wires:
        visited = [True if i == (a - 1) or i == (b - 1) else False for i in range(n)]
        q = deque([b - 1])
        result = 0
        while q:
            now = q.popleft()
            for g in graph[now]:
                if not visited[g]:
                    q.append(g)
                    visited[g] = True
            result += 1
        answer = min(answer, abs(result - (n - result)))
    return answer


"""
애먹었던 문제.
어떨 때 가장 balance하게 나눌 수 있는가?를 고민했는데 해답들은 대부분 brute force를 쓰더라.
그래서 나도 brute force로 적당히 해결. 그런데 유니온 파인드를 써서도 나중에 더 해봐야지.
"""