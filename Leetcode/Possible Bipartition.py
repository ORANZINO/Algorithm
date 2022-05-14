from typing import List

class Solution:
    def dfs(self, now, visited, graph, color):
        for node in graph[now]:
            if not visited[node]:
                color[node] = not color[now]
                visited[node] = True
                result = self.dfs(node, visited, graph, color)
                if not result:
                    return False
            elif color[node] == color[now]:
                return False
        return True

    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = [[] for _ in range(n + 1)]
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        visited = [False] * (n + 1)
        color = [True] * (n + 1)
        for i in range(1, n + 1):
            if not visited[i]:
                visited[i] = True
                output = self.dfs(i, visited, graph, color)
                if not output:
                    return False
        return True

