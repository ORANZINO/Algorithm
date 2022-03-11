from copy import deepcopy


def solution(info, edges):
    def dfs(now, visited, sheep, wolf):
        nonlocal answer
        answer = max(answer, sheep)
        visited[now] = 1
        for node in tree[now]:
            if visited[node] == -1:
                visited[node] = 0
        for i, v in enumerate(visited):
            if v == 0:
                if info[i] == 0:
                    dfs(i, deepcopy(visited), sheep + 1, wolf)
                elif sheep > (wolf + 1):
                    dfs(i, deepcopy(visited), sheep, wolf + 1)

    tree = [[] for _ in range(len(info))]
    answer = 0
    for a, b in edges:
        tree[a].append(b)

    dfs(0, [-1] * len(info), 1, 0)

    return answer