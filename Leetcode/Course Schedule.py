import collections
from typing import *

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)

        trace, visited = set(), set()

        def dfs(i):
            if i in trace:
                return False
            if i in visited:
                return True
            trace.add(i)
            for g in graph[i]:
                if not dfs(g):
                    return False
            trace.remove(i)
            visited.add(i)
            return True

        for x in list(graph):
            if not dfs(x):
                return False

        return True

